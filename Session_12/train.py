from utils import HouseETL, HouseTrain

def main():

    etl = HouseETL(test_size=0.2, random_state=42)
    housing_labels, housing_prepared_fulltest, scaler_path = etl.etl_pipeline()

    t = HouseTrain(housing_labels=housing_labels,
                   housing_prepared_fulltest=housing_prepared_fulltest,
                   n_estimators=100).train()

if __name__ == "__main__":
    main()