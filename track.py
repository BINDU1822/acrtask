# import azure.functions as func
# from azure.identity import DefaultAzureCredential
# from azure.mgmt.resource import SubscriptionClient
# import requests
import os
# import logging
from azure.data.tables import TableServiceClient, TableClient



list_entities = []
second_list = []
def tables_in_account():
        # Instantiate the TableServiceClient from a connection string
        connstr = "DefaultEndpointsProtocol=https;AccountName=opysparkstg;AccountKey=dK+2czDbJPwWx6LzXa4+3t62kz6aW9xQX5dRey5M+htdcKISkMBvG7Pq+Ls5OkJiSGXpyo9txXMe+ASttGZo1Q==;EndpointSuffix=core.windows.net"
        # connstr = os.getenv('CONNECTION_STRING')
        with TableServiceClient.from_connection_string(conn_str=connstr) as table_service:
            list_tables = table_service.list_tables()
            for table in list_tables:
                print(table.name)

        
        with TableClient.from_connection_string(conn_str=connstr, table_name="PySparktable") as table_client:
            for entity in table_client.list_entities():
                list_entities.append(entity)
                # print(entity)
        with TableClient.from_connection_string(conn_str=connstr, table_name="PySparkInfratable") as table_client:
            for entity in table_client.list_entities(): 
                second_list.append(entity)
                # print(entity)
        
tables_in_account() 
