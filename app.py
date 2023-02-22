from flask import Flask,render_template
from templates.track import list_entities,second_list
# from collections import defaultdict
from datetime import datetime

app = Flask(__name__)
# def tables(list_entities):




# return [table_headers,unique_array]


# headers, table = table(list_entities)
def tables(list_entities):
    table_row = []
    sorted_data = sorted(list_entities, key=lambda item: item['RowKey'],reverse=True)
    table_headers = list_entities[0].keys()
    table_latest = set()
    for row in sorted_data:
        values=row.values()
        table_row.append(values)

    unique_array = []
    unique_names = {}
    for d in list_entities:
        if d['DatabricksWorkspace'] in unique_names:
            # if datetime.strptime(unique_names[d['DatabricksWorkspace']]['RowKey'], '%Y-%m-%dT%H:%M:%S%z') < datetime.strptime(d['RowKey'], '%Y-%m-%dT%H:%M:%S%z'):
            if unique_names[d['DatabricksWorkspace']]['RowKey'] < d['RowKey']:
                unique_names[d['DatabricksWorkspace']] = d
        else:
            unique_names[d['DatabricksWorkspace']] = d
    result = list(unique_names.values())
    print(unique_names)


    for outer_key, inner_dict in unique_names.items(): 
        empty_array = list(inner_dict.values())
        unique_array.append(empty_array)

    return unique_array,table_headers



@app.route("/")
def table_one():
    title= "Pyspark table"
    unique_array, table_headers = tables(list_entities)
    return render_template("index.html", table_headers=table_headers, table_row=unique_array,title = title)

@app.route("/PySparkInfra-table")
def table_two():
    title="Pyspark Infra table"
    unique_array, table_headers = tables(second_list)
    return render_template("index.html", table_headers=table_headers, table_row=unique_array,title = title)

# @app.route("/")
# def home():
#     return "hello"