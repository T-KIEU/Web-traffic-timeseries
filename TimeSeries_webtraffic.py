# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 20:46:58 2023

@author: kieu_
"""


import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from lazypredict.Supervised import LazyRegressor



data = pd.read_csv(r"C:\Users\kieu_\OneDrive\Desktop\Project\Data Science\VietNguyen\ML_9-1\Datasets\web-traffic.csv")

# Convertir en date et au bon format
data["date"] = pd.to_datetime(data["date"])
data["date"] = data["date"].dt.strftime("%d/%m/%y")


# Afficher une représentation graphique
fig, ax = plt.subplots()
ax.plot(data["date"], data["users"])
ax.set_xlabel("Date")
ax.set_label("Users")
plt.legend()
plt.show();



# Créer de nouvelles colonnes users en décalant les valeurs users
def create_recursive_data(data, window_size, target_name):
    i = 1
    while i < window_size:
        data["users_{}".format(i)] = data["users"].shift(-i)
        i += 1
    data[target_name] = data["users"].shift(-i)
    
    # Enlever les na situés à la fin du dataset, cela est lié au décalage vers les nouvelles colonnes users
    data = data.dropna(axis=0)
    
    return data



target = "target"
window_size = 10
data = create_recursive_data(data, window_size, target)


X = data.drop([target, "date"], axis=1)
y = data[target]


# Dans les time series, la division en train et test se fait différemment en respectant l'ordre chronologique (80% des données du début pour le train, puis 20% dernières données en test)
# Il ne faut pas utiliser train_test_split qui divise les données de manière aléatoire

train_size = 0.8
num_samples = len(X)

X_train = X[:int(num_samples * train_size)]
y_train = y[:int(num_samples * train_size)]
X_test = X[int(num_samples * train_size):]
y_test = y[int(num_samples * train_size):]


### Lazypredict
reg = LazyRegressor(verbose=0, ignore_warnings=False, custom_metric=None)
models, pred = reg.fit(X_train, X_test, y_train, y_test)
models

#                                Adjusted R-Squared  ...  Time Taken
# Model                                              ...            
# ExtraTreesRegressor                          0.90  ...        0.12
# LGBMRegressor                                0.89  ...        0.29
# HistGradientBoostingRegressor                0.88  ...        0.23
# RandomForestRegressor                        0.88  ...        0.17
# KNeighborsRegressor                          0.88  ...        0.01



knn_reg = KNeighborsRegressor()


params = {
    "n_neighbors": [5, 10, 15],
    "leaf_size": [30, 40, 50],
    "metric": ["minkowski", "manhattan", "chebyshev"],
}


grid_search = RandomizedSearchCV(
    estimator=knn_reg,
    param_distributions=params,
    scoring="f1_weighted",
    cv=5,
    n_jobs=1,
    verbose=1,
    n_iter=30
)


grid_search.fit(X_train, y_train)


y_predict = grid_search.predict(X_test)

print(grid_search.best_params_)
print(grid_search.best_score_)

# {'n_neighbors': 5, 'metric': 'minkowski', 'leaf_size': 30}
# nan


print("R2: {}".format(r2_score(y_test, y_predict)))
print("MSE: {}".format(mean_squared_error(y_test, y_predict)))
print("MAE: {}".format(mean_absolute_error(y_test, y_predict)))

# R2: 0.8913640830861985
# MSE: 65086.80578313254
# MAE: 186.72289156626508


for i, j in zip(y_predict, y_test):
    print("Prediction: {}. Actual value: {}".format(i, j))


fig, ax = plt.subplots()
ax.plot(data["date"][:int(num_samples * train_size)], data["users"][:int(num_samples * train_size)], label="Train")
ax.plot(data["date"][int(num_samples * train_size):], data["users"][int(num_samples * train_size):], label="Test")
ax.plot(data["date"][int(num_samples * train_size):], y_predict, label="Prediction")
ax.set_xlabel("Date")
ax.set_ylabel("Users")
ax.legend()
ax.grid()
plt.show();


