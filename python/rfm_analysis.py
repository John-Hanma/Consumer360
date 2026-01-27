from basket.association_rules import run_market_basket_analysis
from rfm.rfm_validation import validate_rfm_segments
import os
import pandas as pd
from sqlalchemy import create_engine

from rfm.rfm_segmentation import assign_rfm_scores, assign_rfm_segments

print("CURRENT WORKING DIRECTORY:", os.getcwd())

# Database connection (temporary dependency until Week 1 completes)
engine = create_engine(
        "mysql+pymysql://root:Jagan%40074920@localhost/consumer360"

)

# Load Customer 360 data
df = pd.read_sql("SELECT * FROM single_customer_view", engine)

# Apply RFM scoring and segmentation
df = assign_rfm_scores(df)
df = assign_rfm_segments(df)

validation_df = validate_rfm_segments(df)

validation_df.to_csv(
    "data/processed/rfm_segment_validation.csv",
    index=False
)

# Load transaction-level data for Market Basket Analysis
transactions_df = pd.read_sql(
    "SELECT transaction_id, product_name FROM mba_transactions",
    engine
)

# Run Market Basket Analysis
basket_rules = run_market_basket_analysis(transactions_df)
# Filter to strong, actionable rules
basket_rules = basket_rules[basket_rules['lift'] >= 2].head(25)

basket_rules.to_csv(
    "data/processed/market_basket_rules.csv",
    index=False
)
# Save MBA output
basket_rules.to_csv(
    "data/processed/market_basket_rules.csv",
    index=False
)

# Save processed output
df.to_csv(
    "data/processed/rfm_scored_customers.csv",
    index=False
)

print("RFM analysis completed successfully.")
