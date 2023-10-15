# pip install pandas

import pandas as pd

# Replace 'your_file.csv' with the
# actual file path of your CSV file
file_path = "netflix_titles.csv"

# Read the CSV file into a
# pandas DataFrame, keeping the
# header row
df = pd.read_csv(file_path)

# describes the numeric columns
print(df.describe())

# Print column headings
# (column names)
print("Column Headings:")
for column_name in df.columns:
    print(column_name)

# Filter by type, print
# subset of columns
df1 = df[df["type"] == "Movie"]
print(df1[["type", "title"]])

# Filter by type and
# release year
# print a subset of columns
df1 = df[
    (df["type"] == "Movie")
    & (df["release_year"] > 2014)
]
print(
    df1[
        [
            "type",
            "title",
            "release_year",
        ]
    ]
)

# Filter by type, release year
# and rating
# print a subset of columns
df1 = df[
    (
        (df["type"] == "Movie")
        & (df["release_year"] > 2014)
    )
    | (
        df["rating"].isin(
            ["TV-14", "TV-PG"]
        )
    )
]
print(
    df1[
        [
            "type",
            "title",
            "release_year",
            "rating",
        ]
    ]
)

# Filter to get first 2 rows
# print all columns
df1 = df.head(2)
print(df1)

# Save to csv all columns
df1.to_csv(
    "netflix_data.csv", index=False
)

