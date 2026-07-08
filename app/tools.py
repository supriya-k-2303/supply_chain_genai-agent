import pandas as pd

CSV_PATH = "data/supply_chain_enriched.csv"


def load_supply_chain_data():
    return pd.read_csv(CSV_PATH)


def get_delivery_context():

    df = load_supply_chain_data()

    delayed = df[
        df["DeliveryStatus"].isin(
            ["Delayed", "Slightly Delayed"]
        )
    ]

    total = len(delayed)

    percentage = round(
        (total / len(df)) * 100,
        2
    )

    return f"""
Delivery Analysis

Total Records:
{len(df)}

Total Delayed Deliveries:
{total}

Delayed Percentage:
{percentage}%
"""


def get_inventory_context():

    df = load_supply_chain_data()

    return f"""
Inventory Analysis

Total Products:
{df["ProductID"].nunique()}

Total Inventory Quantity:
{df["Quantity"].sum()}

Average Inventory Level:
{round(df["InventoryLevel"].mean(),2)}

Top Product Categories:

{df["ProductCategory"].value_counts().head(10).to_string()}
"""


def get_supplier_context():

    df = load_supply_chain_data()

    return f"""
Supplier Analysis

Total Suppliers:
{df["SupplierID"].nunique()}

Average Supplier Rating:
{round(df["SupplierRating"].mean(),2)}

Top Suppliers:

{df["SupplierName"].value_counts().head(5).to_string()}
"""


def get_sales_context():

    df = load_supply_chain_data()

    return f"""
Sales Analysis

Total Sales:
{round(df["Sales"].sum(),2)}

Average Order Value:
{round(df["Sales"].mean(),2)}

Total Orders:
{df["OrderID"].nunique()}
"""