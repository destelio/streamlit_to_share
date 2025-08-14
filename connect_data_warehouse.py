

import duckdb


from constants import DATA_WAREHOUSE_PATH


conn = duckdb.connect(DATA_WAREHOUSE_PATH)

#print("DATA_WAREHOUSE_PATH", DATA_WAREHOUSE_PATH)


def query_dwh(query:str = "SELECT * FROM stagging_table.cars" ):
            with duckdb.connect(DATA_WAREHOUSE_PATH) as conn:
                return conn.query(query).df()

steg1 = 1

def query_dwh_price(query:str = f"SET VARIABLE my_var = 2; SELECT cleaned_price FROM stagging_table.cars where cleaned_bedrooms = 2" ):
            #with duckdb.connect(DATA_WAREHOUSE_PATH) as conn:
            return conn.query(query).df()


def execute_query(query: str, return_type: str = "df"):
    with duckdb.connect(DATA_WAREHOUSE_PATH) as conn:
        if return_type == "df":
            return conn.execute(query).df()
        elif return_type == "arrow":
            return conn.execute(query).arrow()
        elif return_type == "list":
            return conn.execute(query).fetchall()


#destination_table_name = "orders"
#data = execute_query(f"select * from {destination_table_name}", return_type="df")

