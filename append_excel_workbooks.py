# pip3 install pandas
# pip3 install openpyxl

import os
import pandas as pd


def append_workbooks(
    directory: str = ".",
    sheet_name: str = "Sheet1",
) -> None:
    """Appends Excel workbooks
       into a single workbook
    Arguments
    directory: directory where
               Excel workbooks
               are located,
               defaults to .

    sheet_name: the sheet name
                of the workbooks,
                defaults to Sheet1
    """

    df = pd.DataFrame()

    # loop over Excel workbooks
    for file in os.listdir(directory):
        if (
            file.endswith(".xlsx")
            and not file.startswith("~")
            and not file.startswith(
                "ALL_DATA"
            )
        ):
            file_path = os.path.join(
                directory, file
            )
            data = pd.read_excel(
                file_path, sheet_name
            )
            df = pd.concat([df, data])

    file_path = os.path.join(
        directory, "ALL_DATA.xlsx"
    )
    df.to_excel(file_path, index=False)


append_workbooks(
    directory="Transactions",
    sheet_name="Sheet1",
)
