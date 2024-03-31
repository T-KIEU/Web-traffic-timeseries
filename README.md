# Web-traffic-timeseries
Prediction of the trend in the number of users visiting the website

## Dataset
Here is part of the dataset:

| date | users |
| --- | ---|
| 1/7/2020 | 2324 |
| 2/7/2020 | 2201 |
| 3/7/2020 | 2146 |
| 4/7/2020 | 1666 |
| 5/7/2020 | 1433 |
| 6/7/2020 | 2195 |
| 7/7/2020 | 2240 |
| 8/7/2020 | 2295 |
| 9/7/2020 | 2279 |
| 10/7/2020 |	2155 |
| 11/7/2020 |	1737 |
| 12/7/2020 |	1391 |
| 13/7/20 |	2150 |
| 14/7/20 |	2121 |
| 15/7/20 |	2136 |
| 16/7/20 |	2166 |
| 17/7/20 |	2067 |
| 18/7/20 |	1648 |
| 19/7/20 |	1401 |
| 20/7/20 |	2040 |
| 21/7/20 |	2269 |
| 22/7/20 |	2283 |
| 23/7/20 |	2174 |
| 24/7/20 |	2178 |
| 25/7/20 |	1659 |
| 26/7/20 |	1338 |
| 27/7/20 |	2041 |
| 28/7/20 |	2162 |
| 29/7/20 |	2123 |
| 30/7/20 |	2147 |
| 31/7/20 |	2124 |


## Pre-processing
* Convert the date in the right format <br />
* Remove NA values <br />
<br />

Let's visualize the dataset: <br />
![image](https://github.com/T-KIEU/Web-traffic-timeseries/assets/100022674/db113ba0-83b4-4dd3-830e-fee83efedbfa)


## Training

Train and compare many models: <br />
| Model | Adjusted R-Squared | ... | Time Taken |
| --- | --- | --- | --- |
| ExtraTreesRegressor | 0.90 | ... | 0.12 |
| LGBMRegressor | 0.89 | ... | 0.29 |
| HistGradientBoostingRegressor | 0.88 | ... | 0.23 |
| RandomForestRegressor | 0.88 | ... | 0.17 |
| KNeighborsRegressor | 0.88 | ... | 0.01 |
| ... |

According to the results above, KNeighborsRegressor model seems to be the best one for its precision as well as its time record. <br />
<br />

Parameters: <br />
* n_neighbors : [5, 10, 15] <br />
* leaf_size: [30, 40, 50] <br />
* metric: ["minkowski", "manhattan", "chebyshev"] <br />
<br />

Performances: <br />
R2: 0.8913640830861985 <br />
MSE: 65086.80578313254 <br />
MAE: 186.72289156626508 <br />
<br />

Let's visualize the prediction: <br />
![image](https://github.com/T-KIEU/Web-traffic-timeseries/assets/100022674/fa061f28-87b7-45b7-bf6b-c528fbd3557d)

