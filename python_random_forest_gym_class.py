# pip install numpy
# pip install pandas
# pip install matplotlib
# pip install -U scikit-learn
# pip install -U imbalanced-learn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

from sklearn.model_selection import (
    train_test_split,
)

from imblearn.over_sampling import (
    RandomOverSampler,
)

from sklearn.ensemble import (
    RandomForestClassifier,
)

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
)

# Load data
data_df = pd.read_csv(
    "fitness_class_2212.csv"
)

# See the data
print(data_df)

# See the column data types
print(data_df.dtypes)

# Check counts of null
# values in data
print(data_df.isnull().sum())

# Check target variable -
# imbalanced dataset?
# There are more not
# attended than attended
# data points
data_count_df = data_df.groupby(
    ["attended"]
)["attended"].count()
print(data_count_df)

# Convert days_before
# feature to numeric
data_df["days_before"] = pd.to_numeric(
    data_df["days_before"],
    errors="coerce",
)

# Convert attended
# feature to numeric
data_df["attended"] = pd.to_numeric(
    data_df["attended"], errors="coerce"
)

# Drop any data rows
# with null values
data_df = data_df.dropna()

# Extract target to predict
y = data_df.pop("attended")

# Drop features not
# required in model
data_df = data_df.drop(
    ["category", "booking_id"], axis=1
)

# See if day_of_week column
# has unique values for each
# day of the week
print(
    data_df[
        "day_of_week"
    ].value_counts()
)

# Clean up day_of_week to
# have single value per day
data_df.loc[
    data_df["day_of_week"].isin(
        ["Fri."]
    ),
    "day_of_week",
] = "Fri"
data_df.loc[
    data_df["day_of_week"].isin(
        ["Wednesday"]
    ),
    "day_of_week",
] = "Wed"
data_df.loc[
    data_df["day_of_week"].isin(
        ["Monday"]
    ),
    "day_of_week",
] = "Mon"

# See if time column
# has unique values
# for AM and PM
print(data_df["time"].value_counts())

# Get list of
# categorical features
# to convert to
# dummy variables
# (one-hot encoding)
features_to_encode = list(
    data_df.select_dtypes(
        include=["object"]
    ).columns
)
print(features_to_encode)

# Format categorical
# features to one-hot
# encoding
# leave numeric
# features unchanged
x = pd.get_dummies(
    data_df, columns=features_to_encode
)

# Create train and test data
# Seed means the result
# is reproducible
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

# Dataset is imbalanced,
# to create balanced data
# Decided to randomly
# over sample the
# minority class
ros = RandomOverSampler(random_state=12)
(
    x_train_ros,
    y_train_ros,
) = ros.fit_resample(x_train, y_train)
print(
    sorted(Counter(y_train_ros).items())
)


# Created and train RF model
# 250 decision trees
# were trained in the model
rf_classifier = RandomForestClassifier(
    min_samples_leaf=50,
    n_estimators=250,
    bootstrap=True,
    oob_score=True,
    n_jobs=-1,
    random_state=seed,
)
rf_classifier.fit(
    x_train_ros, y_train_ros
)


# Predicted the test
# data target attended
y_pred = rf_classifier.predict(x_test)

# Output the accuracy
# using predictions
# and known test
# data attended values
accuracy_score(y_test, y_pred)
print(
    f"Accuracy= "
    f"{round(accuracy_score(y_test,y_pred),3)*100} %"
)

# Output additional metrics
print(
    classification_report(
        y_test, y_pred
    )
)

# Plotted the models most important features
# Larger importance values mean more important
feat_importances = pd.Series(
    rf_classifier.feature_importances_,
    index=x_train.columns,
)
feat_importances.nlargest(15).plot(
    kind="barh"
)
plt.title("Top 15 important features")
plt.show()
