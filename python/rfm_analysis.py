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

# Save processed output
df.to_csv(
    "data/processed/rfm_scored_customers.csv",
    index=False
)

print("RFM analysis completed successfully.")