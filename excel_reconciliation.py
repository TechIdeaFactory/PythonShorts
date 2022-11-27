# pip install pandas
# pip install openpyxl
# pip install xlsxwriter

import pandas as pd
import numpy as np

N = 100
transaction_a_df = pd.read_excel(
    "Transactions_A.xlsx",
    sheet_name="Transactions",
    dtype={
        "Transaction Number": str,
        "Amount": float,
    },
)
transaction_a_df[
    "Amount_Round"
] = np.round(
    transaction_a_df.Amount * N
).astype(
    int
)
# print(transaction_a_df)

transaction_b_df = pd.read_excel(
    "Transactions_B.xlsx",
    sheet_name="Transactions",
    dtype={
        "Transaction Number": str,
        "Amount": float,
    },
)
transaction_b_df[
    "Amount_Round"
] = np.round(
    transaction_b_df.Amount * N
).astype(
    int
)
# print(transaction_b_df.info())

matches_df = pd.merge(
    transaction_a_df,
    transaction_b_df,
    how="inner",
    on=[
        "Transaction Number",
        "Customer",
        "Date",
        "Product",
        "Amount_Round",
    ],
)
matches_df = matches_df[
    [
        "Transaction Number",
        "Customer",
        "Date",
        "Product",
        "Amount_x",
    ]
]
matches_df = matches_df.rename(
    columns={"Amount_x": "Amount"}
)
# print(matches_df)

diffs_df = pd.merge(
    transaction_a_df,
    transaction_b_df,
    how="inner",
    on=["Transaction Number"],
)
diffs_df = diffs_df[
    (
        diffs_df["Customer_x"]
        != diffs_df["Customer_y"]
    )
    | (
        diffs_df["Date_x"]
        != diffs_df["Date_y"]
    )
    | (
        diffs_df["Product_x"]
        != diffs_df["Product_y"]
    )
    | (
        diffs_df["Amount_Round_x"]
        != diffs_df["Amount_Round_y"]
    )
]
diffs_df = diffs_df[
    [
        "Transaction Number",
        "Customer_x",
        "Customer_y",
        "Date_x",
        "Date_y",
        "Product_x",
        "Product_y",
        "Amount_x",
        "Amount_y",
    ]
]
diffs_df = diffs_df.rename(
    columns={
        "Customer_x": "Customer_A",
        "Customer_y": "Customer_B",
        "Date_x": "Date_A",
        "Date_y": "Date_B",
        "Product_x": "Product_A",
        "Product_y": "Product_B",
        "Amount_x": "Amount_A",
        "Amount_y": "Amount_B",
    }
)
# print(diffs_df)

missing_b_df = pd.merge(
    transaction_a_df,
    transaction_b_df,
    how="left",
    on=["Transaction Number"],
)
missing_b_df = missing_b_df[
    missing_b_df["Customer_y"].isna()
]
missing_b_df = missing_b_df[
    [
        "Transaction Number",
        "Customer_x",
        "Date_x",
        "Product_x",
        "Amount_x",
    ]
]
missing_b_df = missing_b_df.rename(
    columns={
        "Customer_x": "Customer",
        "Date_x": "Date",
        "Product_x": "Product",
        "Amount_x": "Amount",
    }
)
print(missing_b_df)

missing_a_df = pd.merge(
    transaction_b_df,
    transaction_a_df,
    how="left",
    on=["Transaction Number"],
)
missing_a_df = missing_a_df[
    missing_a_df["Customer_y"].isna()
]
missing_a_df = missing_a_df[
    [
        "Transaction Number",
        "Customer_x",
        "Date_x",
        "Product_x",
        "Amount_x",
    ]
]
missing_a_df = missing_a_df.rename(
    columns={
        "Customer_x": "Customer",
        "Date_x": "Date",
        "Product_x": "Product",
        "Amount_x": "Amount",
    }
)
print(missing_a_df)

writer = pd.ExcelWriter(
    "Reconciliation.xlsx",
    engine="xlsxwriter",
)

matches_df.to_excel(
    writer,
    sheet_name="Matches",
    index=False,
)
diffs_df.to_excel(
    writer,
    sheet_name="Diffs",
    index=False,
)
missing_a_df.to_excel(
    writer,
    sheet_name="Missing in A",
    index=False,
)
missing_b_df.to_excel(
    writer,
    sheet_name="Missing in B",
    index=False,
)

writer.save()
