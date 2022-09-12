# pip install pandas
# pip install sklearn

import pandas as pd
from sklearn.model_selection import (
    train_test_split,
)
from sklearn import linear_model
from sklearn.metrics import (
    mean_squared_error,
)

data = pd.read_csv(
    "Space_Corrected.csv"
)
data = data.dropna()
data["Year"] = pd.to_datetime(
    data["Datum"], utc=True
).dt.year
data = pd.get_dummies(
    data, columns=["Company Name"]
)
data["Country"] = (
    data["Location"]
    .str.rsplit(",")
    .str[-1]
)
data = pd.get_dummies(
    data, columns=["Country"]
)
data = data.drop(
    [
        "Unnamed: 0.1",
        "Unnamed: 0",
        "Location",
        "Datum",
        "Detail",
        "Status Rocket",
        "Status Mission",
    ],
    axis=1,
)
data = data.apply(
    pd.to_numeric, errors="coerce"
)
data = data.dropna()
y_data = data[" Rocket"]
x_data = data.drop([" Rocket"], axis=1)
(
    x_train,
    x_test,
    y_train,
    y_test,
) = train_test_split(
    x_data,
    y_data,
    test_size=0.2,
    random_state=1,
)
print(len(x_test))
print(x_test.head())
print(len(y_test))
print(y_test.head())
reg_model = (
    linear_model.LinearRegression()
)
reg_model.fit(x_train, y_train)
pred_y = reg_model.predict(x_test)
print(pred_y[102])
print(y_test.iloc[102])
mse = mean_squared_error(y_test, pred_y)
print(mse)
