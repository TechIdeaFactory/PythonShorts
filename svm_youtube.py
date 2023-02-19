# pip install pandas
# pip install -U scikit-learn
# pip install -U imbalanced-learn

import pandas as pd
import numpy as np

from sklearn.preprocessing import (
    MinMaxScaler,
)

from imblearn.over_sampling import (
    RandomOverSampler,
)

from sklearn.model_selection import (
    train_test_split,
)

from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
)

from sklearn.metrics import (
    classification_report,
)

from collections import Counter

# Load YouTube data
data_df = pd.read_csv(
    "most_subscribed_youtube_channels.csv"
)

# Convert columns to integer type
data_df["subscribers_n"] = (
    data_df["subscribers"]
    .str.replace(",", "")
    .astype(int)
)
data_df["video_views_n"] = (
    data_df["video views"]
    .str.replace(",", "")
    .astype(int)
)
data_df["video_count_n"] = (
    data_df["video count"]
    .str.replace(",", "")
    .astype(int)
)

# Drop rows with null value columns
data_df.dropna(inplace=True)

# Create target_class to predict
data_df["target_class"] = np.where(
    data_df["subscribers_n"]
    >= 20000000,
    1,
    0,
)

# Note an imbalanced data set
print(
    data_df[
        "target_class"
    ].value_counts()
)

# Note row counts for category vary
print(
    data_df["category"].value_counts()
)

# Create one-hot encodings for
# the different category values
data_df["category_s"] = data_df[
    "category"
]
data_df = pd.get_dummies(
    data_df, columns=["category_s"]
)

# SVM model features
# should be scaled
data_df["started_s"] = data_df[
    "started"
]
data_df["video_views_s"] = data_df[
    "video_views_n"
]
data_df["video_count_s"] = data_df[
    "video_count_n"
]

scaler = MinMaxScaler()
data_df[
    [
        "started_s",
        "video_views_s",
        "video_count_s",
    ]
] = scaler.fit_transform(
    data_df[
        [
            "started_s",
            "video_views_s",
            "video_count_s",
        ]
    ]
)

# Filter out YouTube channels
# with zero video views
data_df = data_df[
    data_df["video_views_n"] >= 1
]

# Target class to predict
y = data_df.pop("target_class")

# Prepare SVM model features
# dropping columns not required
# Models features are category
# one-hot encodings and
# scaled features for started,
# video views and video counts
x = data_df.drop(
    [
        "rank",
        "Youtuber",
        "subscribers",
        "video views",
        "video count",
        "category",
        "started",
        "subscribers_n",
        "video_views_n",
        "video_count_n",
    ],
    axis=1,
)

# Get training and test data sets
# Seed means the result is reproducible
seed = 10
(
    x_train,
    x_test,
    y_train,
    y_test,
) = train_test_split(
    x,
    y,
    test_size=0.333,
    random_state=seed,
)

# Data set is imbalanced,
# to create balanced data set
# randomly over sample
# the minority class
ros = RandomOverSampler(random_state=12)
(
    x_train_ros,
    y_train_ros,
) = ros.fit_resample(x_train, y_train)
print(
    sorted(Counter(y_train_ros).items())
)

# instantiate SVM classifier with
# default hyperparameters
svc = SVC()

# fit classifier to training set
svc.fit(x_train_ros, y_train_ros)

# make predictions on test set
y_pred = svc.predict(x_test)

# compute and print accuracy score
print(
    "Model accuracy score : {0:0.4f}".format(
        accuracy_score(y_test, y_pred)
    )
)

# compute and print precison, recall
# and F1 score
print(
    classification_report(
        y_test, y_pred
    )
)
