import pandas as pd


def validate_rfm_segments(df):
    """
    Perform statistical validation of RFM segments.
    Returns a summary DataFrame.
    """

    validation_df = (
        df.groupby("RFM_segment")
        .agg(
            customer_count=("RFM_segment", "count"),
            avg_revenue=("monetary", "mean"),
            avg_frequency=("frequency", "mean"),
            avg_recency_days=("recency_days", "mean")
        )
        .reset_index()
        .sort_values(by="avg_revenue", ascending=False)
    )

    return validation_df
