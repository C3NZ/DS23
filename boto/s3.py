import sqlite3 as lite

import boto3
import pandas as pd


def list_buckets():
    # Retrieve the list of existing buckets
    s3 = boto3.client("s3")
    response = s3.list_buckets()

    # Output the bucket names
    print("Existing buckets:")
    for bucket in response["Buckets"]:
        print(f'  {bucket["Name"]}')


def read_csv():
    s3 = boto3.resource("s3")
    csv = s3.Object("make-data", "Churn_Modelling.csv")
    body = csv.get()["Body"].read()
    print(body)


def get_csv_with_client():
    s3 = boto3.client("s3")
    csv = s3.get_object(Bucket="make-data", Key="Churn_Modelling.csv")
    df = pd.read_csv(csv["Body"])
    return df


def create_table(con):
    with con:
        curr = con.cursor()
        curr.execute(
            "CREATE TABLE Population(id INTEGER PRIMARY KEY, country TEXT, population INT)"
        )
        curr.execute("INSERT INTO Population VALUES(NULL, 'Germany', 811975432)")
        curr.execute("INSERT INTO Population VALUES(NULL, 'France', 664151324)")
        curr.execute("INSERT INTO Population VALUES(NULL, 'Spain', 46439864)")
        curr.execute("INSERT INTO Population VALUES(NULL, 'Italy', 60797343)")
        curr.execute("INSERT INTO Population VALUES(NULL, 'Spain', 46439864)")


def main():
    df = get_csv_with_client()

    con = lite.connect("population.db")

    # create_table(con)

    query = "SELECT country FROM Population WHERE country LIKE 'S%';"

    df = pd.read_sql_query(query, con)
    print(df)


if __name__ == "__main__":
    main()
