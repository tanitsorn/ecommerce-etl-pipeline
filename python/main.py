from python.transform.transform_pipeline import run_transform_pipeline
from python.load.load_to_mysql import load_to_mysql

def main():

    print("========== ETL Pipeline ==========")

    print("Step 1 : Transform")
    run_transform_pipeline()

    print("Step 2 : Load")
    load_to_mysql()

    print("ETL Pipeline Finished!")

if __name__ == "__main__":
    main()