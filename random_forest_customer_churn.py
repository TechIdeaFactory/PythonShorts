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
data_df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
# View data
print(data_df.head())
# Check target variable - imbalanced dataset?
data_count_df = data_df.groupby(["Churn"])["Churn"].count()
print(data_count_df)
# Check counts of null values in data
print(data_df.isnull().sum())
# Format target variable to 1 or 0
churn_map = {"Yes": 1, "No": 0}
data_df["ChurnStatus"] = data_df["Churn"].map(churn_map)
# Convert TotalCharges feature to numeric
data_df["TotalCharges"] = pd.to_numeric(data_df["TotalCharges"], errors="coerce")
# Drop any data rows with null values
data_df = data_df.dropna()
# Extract target to predict
y = data_df.pop("ChurnStatus")
# Drop features not required in model
data_df = data_df.drop(["customerID", "Churn"], axis=1)
# Get list of categorical features
# to convert to dummy variables (one-hot encoding)
features_to_encode = list(data_df.select_dtypes(include=["object"]).columns)
# Format categorical features to one-hot encoding
# leave numeric features unchanged
x = pd.get_dummies(data_df, columns=features_to_encode)
# Create train and test data
# Seed means the result is reproducible
seed = 10
(
    x_train,
    x_test,
    y_train,
    y_test,
) = train_test_split(x, y, test_size=0.333, random_state=seed)
# Dataset is imbalanced, to create balanced data
# Decided to randomly over sample the minority class
ros = RandomOverSampler(random_state=12)
x_train_ros, y_train_ros = ros.fit_resample(x_train, y_train)
print(sorted(Counter(y_train_ros).items()))
# Created and trained RF model
# 250 decision trees were trained in the model
rf_classifier = RandomForestClassifier(
    min_samples_leaf=50,
    n_estimators=250,
    bootstrap=True,
    oob_score=True,
    n_jobs=-1,
    random_state=seed,
)
rf_classifier.fit(x_train_ros, y_train_ros)
# Predicted the test data target ChurnStatus
# Output the accuracy using predictions
# and known test data ChurnStatus values
y_pred = rf_classifier.predict(x_test)
accuracy_score(y_test, y_pred)
print(f"Accuracy= {round(accuracy_score(y_test,y_pred),3)*100} %")
# Output additional metrics
print(classification_report(y_test, y_pred))
# Plotted the models most important features
# Larger importance values mean more important
feat_importances = pd.Series(
    rf_classifier.feature_importances_,
    index=x_train.columns,
)
feat_importances.nlargest(15).plot(kind="barh")
plt.title("Top 15 important features")
plt.show()
