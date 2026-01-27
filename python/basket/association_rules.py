import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules


def run_market_basket_analysis(df):
    """
    Perform Market Basket Analysis using Apriori.
    Optimized to prevent memory explosion.
    """

    # Limit to top products (critical for performance)
    top_products = (
        df['product_name']
        .value_counts()
        .head(200)
        .index
    )
    df = df[df['product_name'].isin(top_products)]

    # Build basket (transaction x product)
    basket = (
        df
        .groupby(['transaction_id', 'product_name'])['product_name']
        .count()
        .unstack()
        .fillna(0)
    )

    # Convert to boolean (mlxtend recommended)
    basket = basket > 0

    # Generate frequent itemsets
    frequent_itemsets = apriori(
        basket,
        min_support=0.02,
        use_colnames=True
    )

    # Generate association rules
    rules = association_rules(
        frequent_itemsets,
        metric="lift",
        min_threshold=1
    )

    # Sort strongest rules first
    rules = rules.sort_values(by="lift", ascending=False)

    return rules