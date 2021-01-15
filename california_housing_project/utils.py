import os
import pathlib
import tarfile
import urllib.request
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from pickle import dump, load
from sklearn.ensemble import RandomForestRegressor


class DataFetch(object):
    """
    Class for "Get the Data" in the notebook"
    """

    def __init__(self):
        self.DOWNLOAD_ROOT = "https://raw.githubusercontent.com/vfp1/bts-dsf-2020/main/"
        self.HOUSING_PATH = os.path.join(str(pathlib.Path().absolute()), "housing")
        self.HOUSING_URL = self.DOWNLOAD_ROOT + "data/housing.tgz"

    def fetch_housing_data(self):
        if not os.path.isdir(self.HOUSING_PATH):
            os.makedirs(self.HOUSING_PATH)

        tgz_path = os.path.join(self.HOUSING_PATH, "housing.tgz")
        urllib.request.urlretrieve(self.HOUSING_URL, tgz_path)
        housing_tgz = tarfile.open(tgz_path)
        housing_tgz.extractall(path=self.HOUSING_PATH)
        housing_tgz.close()

        return self.HOUSING_PATH

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
        # column index
        self.rooms_ix = 3
        self.bedrooms_ix = 4
        self.population_ix = 5
        self.households_ix = 6
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self  # nothing else to do

    def transform(self, X):
        rooms_per_household = X[:, self.rooms_ix] / X[:, self.households_ix]
        population_per_household = X[:, self.population_ix] / X[:, self.households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, self.bedrooms_ix] / X[:, self.rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,
                         bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

class HouseETL(object):
    """
    Class for all the ETL parts of the project
    """

    def __init__(self, test_size, random_state):

        self.housing_path = DataFetch().fetch_housing_data()
        self.test_size = float(test_size)
        self.random_state = int(random_state)

    def _load_housing_data(self):
        csv_path = os.path.join(self.housing_path, "housing.csv")

        return pd.read_csv(csv_path)

    def _stratified_splits(self):
        global strat_train_set
        global strat_test_set

        self.housing_df = self._load_housing_data()

        self.housing_df["income_cat"] = pd.cut(self.housing_df["median_income"],
                                       bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                       labels=[1, 2, 3, 4, 5])

        split = StratifiedShuffleSplit(n_splits=1,
                                       test_size=self.test_size,
                                       random_state=self.random_state)

        for train_index, test_index in split.split(self.housing_df, self.housing_df["income_cat"]):
            strat_train_set = self.housing_df.loc[train_index]
            strat_test_set = self.housing_df.loc[test_index]

        for set_ in (strat_train_set, strat_test_set):
            set_.drop("income_cat", axis=1, inplace=True)

        return strat_train_set, strat_test_set

    def etl_pipeline(self):

        strat_train_set, strat_test_set = self._stratified_splits()

        housing = strat_train_set.drop("median_house_value", axis=1)
        housing_labels = strat_train_set["median_house_value"].copy()

        housing_num = housing.drop("ocean_proximity", axis=1)

        num_pipeline_fulltest = Pipeline([
            ('imputer', SimpleImputer(strategy="median")),
            ('attribs_adder', CombinedAttributesAdder()),
            ('std_scaler', StandardScaler()),
        ])

        housing_num_tr_fulltest = num_pipeline_fulltest.fit_transform(housing_num)

        num_attribs = list(housing_num)
        cat_attribs = ["ocean_proximity"]

        full_pipeline_fulltest = ColumnTransformer([
            ("num", num_pipeline_fulltest, num_attribs),
            ("cat", OneHotEncoder(), cat_attribs),
        ])

        housing_prepared_fulltest = full_pipeline_fulltest.fit_transform(housing)

        # Save the scaler
        scaler_path = os.path.join(pathlib.Path().absolute(), "scaler")
        scaler_file = scaler_path + "/scaled_features.pkl"

        if not os.path.isdir(scaler_path):
            os.makedirs(scaler_path)
        dump(full_pipeline_fulltest, open(scaler_file, 'wb'))

        return housing_labels, housing_prepared_fulltest, scaler_path

class HouseTrain(object):

    def __init__(self, housing_labels, housing_prepared_fulltest, n_estimators):
        self.housing_labels = housing_labels
        self.housing_prepared = housing_prepared_fulltest
        self.n_estimators = int(n_estimators)

    def train(self):

        forest_reg = RandomForestRegressor(n_estimators=self.n_estimators, random_state=42)
        forest_reg.fit(self.housing_prepared, self.housing_labels)

        # Save the model
        model_path = os.path.join(str(pathlib.Path().absolute()), "model")
        model_file = model_path + "/forest_reg.pkl"

        if not os.path.isdir(model_path):
            os.makedirs(model_path)
        dump(forest_reg, open(model_file, 'wb'))


class HousePredict(object):

    def __init__(self):
        scaler_path = os.path.join(str(pathlib.Path().absolute()), "scaler")
        scaler_file = scaler_path + "/scaled_features.pkl"
        model_path = os.path.join(str(pathlib.Path().absolute()), "model")
        model_file = model_path + "/forest_reg.pkl"

        self.scaler = load(open(scaler_file, 'rb'))
        self.model = load(open(model_file, 'rb'))

    def predict(self, longitude,
                latitude,
                housing_median_age,
                total_rooms,
                total_bedrooms,
                population,
                households,
                median_income,
                ocean_proximity):

        p = pd.DataFrame([longitude,
                          latitude,
                          housing_median_age,
                          total_rooms,
                          total_bedrooms,
                          population,
                          households,
                          median_income,
                          ocean_proximity], index=["longitude",
                                                   "latitude",
                                                   "housing_median_age",
                                                   "total_rooms",
                                                   "total_bedrooms",
                                                   "population",
                                                   "households",
                                                   "median_income",
                                                   "ocean_proximity"]).transpose()

        p_trasnformed = self.scaler.transform(p)
        p_predict = self.model.predict(p_trasnformed)

        return p_predict, p
