import pandas as pd


def assign_rfm_scores(df):
    """
    Assign quintile-based RFM bins and numeric scores.
    Assumes df already contains:
    - recency_days
    - frequency
    - monetary
    """

    df = df.copy()

    # Quantile binning
    df['R_bin'] = pd.qcut(df['recency_days'], q=5, duplicates='drop')
    df['F_bin'] = pd.qcut(df['frequency'], q=5, duplicates='drop')
    df['M_bin'] = pd.qcut(df['monetary'], q=5, duplicates='drop')

    # Convert bins to scores
    # Recency is inverted (lower days = better)
    df['R_score'] = df['R_bin'].cat.codes.max() - df['R_bin'].cat.codes + 1
    df['F_score'] = df['F_bin'].cat.codes + 1
    df['M_score'] = df['M_bin'].cat.codes + 1

    # Combined RFM code
    df['RFM_code'] = (
        df['R_score'].astype(str) +
        df['F_score'].astype(str) +
        df['M_score'].astype(str)
    )

    return df


def assign_rfm_segments(df):
    """
    Assign human-readable RFM segments based on RFM scores.
    """

    def segment(row):
        R, F, M = int(row['R_score']), int(row['F_score']), int(row['M_score'])

        if R >= 4 and F >= 4 and M >= 4:
            return 'Champions'

        elif R >= 3 and F >= 4 and M >= 3:
            return 'Loyal'

        elif R >= 4 and F in [2, 3] and M in [2, 3]:
            return 'Potential Loyalist'

        elif R >= 3 and F >= 3 and M <= 2:
            return 'Price Sensitive'

        elif R in [2, 3] and F in [2, 3] and M in [2, 3]:
            return 'Needs Attention'

        elif R == 2 and F <= 2:
            return 'About to Sleep'

        elif R == 1 and F in [1, 2]:
            return 'Hibernating'

        else:
            return 'Lost'

    df = df.copy()
    df['RFM_segment'] = df.apply(segment, axis=1)

    return df

print("RFM segmentation completed successfully.")