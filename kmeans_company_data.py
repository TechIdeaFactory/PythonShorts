import pandas as pd
import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.cluster import KMeans
from sklearn.preprocessing import (
    StandardScaler,
)

finance_data_df = pd.read_csv(
    "2018_Financial_Data.csv"
)
finance_data_df = finance_data_df[
    [
        "StockID",
        "cashRatio",
        "debtEquityRatio",
    ]
]
finance_data_df = (
    finance_data_df.astype(
        {
            "cashRatio": float,
            "debtEquityRatio": float,
        }
    )
)
finance_data_df.dropna(inplace=True)

# transform data features to
# standard normal distribution
scaler = StandardScaler()
finance_data_df[
    ["cashRatio_S", "debtEquityRatio_S"]
] = scaler.fit_transform(
    finance_data_df[
        ["cashRatio", "debtEquityRatio"]
    ]
)

kmeans_kwargs = {
    "init": "random",
    "n_init": 10,
    "max_iter": 300,
    "random_state": 42,
}

# sse list holds the SSE values for each k
sse = []
for k in range(1, 11):
    kmeans = KMeans(
        n_clusters=k, **kmeans_kwargs
    )
    kmeans.fit(
        finance_data_df[
            [
                "cashRatio_S",
                "debtEquityRatio_S",
            ]
        ]
    )
    sse.append(kmeans.inertia_)

plt.style.use("fivethirtyeight")
plt.plot(range(1, 11), sse)
plt.xticks(range(1, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()

kl = KneeLocator(
    range(1, 11),
    sse,
    curve="convex",
    direction="decreasing",
)
print(kl.elbow)

kmeans = KMeans(
    n_clusters=kl.elbow,
    init="random",
    n_init=10,
)
kmeans.fit(
    finance_data_df[
        [
            "cashRatio_S",
            "debtEquityRatio_S",
        ]
    ]
)
finance_data_df[
    "kmeans"
] = kmeans.labels_

plt.scatter(
    x=finance_data_df["cashRatio"],
    y=finance_data_df[
        "debtEquityRatio"
    ],
    c=finance_data_df["kmeans"],
)
plt.xlabel("cashRatio")
plt.ylabel("debtEquityRatio")
plt.show()
print(
    finance_data_df[
        "kmeans"
    ].value_counts()
)
print(
    finance_data_df[
        ["StockID", "kmeans"]
    ]
)
new_data = dict(
    StockID="TEST",
    cashRatio=0.6,
    debtEquityRatio=1.2,
)
new_data_df = pd.DataFrame(
    new_data, index=[0]
)
new_data_df[
    ["cashRatio_S", "debtEquityRatio_S"]
] = scaler.fit_transform(
    new_data_df[
        ["cashRatio", "debtEquityRatio"]
    ]
)
prediction = kmeans.predict(
    new_data_df[
        [
            "cashRatio_S",
            "debtEquityRatio_S",
        ]
    ]
)
print(
    "Prediction cluster "
    + str(prediction[0])
)
