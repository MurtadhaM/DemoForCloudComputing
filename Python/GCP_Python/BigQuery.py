import json
from google.cloud import bigquery

selected_dataset, selected_project, selected_table,selected_row   =  None, None, None, None

client = bigquery.Client()

def list_projects():
    projects = client.list_projects()
    return projects

def list_datasets():
    client = bigquery.Client(selected_project)
    datasets = client.list_datasets()
    return datasets



def list_tables(dataset_id=selected_dataset, project_id=selected_project):
  dataset = bigquery.Dataset(f"{project_id}.{dataset_id}")
  tables = client.list_tables(dataset)
  return tables



def list_rows(dataset_id=selected_dataset, project_id=selected_project, table_id=selected_table):
  table = bigquery.Table(f"{project_id}.{dataset_id}.{table_id}")
  rows = client.list_rows(table)
  return rows

# function to get the schema of a table
def get_schema(dataset_id=selected_dataset, project_id=selected_project, table_id=selected_table, row_id=selected_row):
  SCHEMA = bigquery.Table(f"{project_id}.{dataset_id}.{table_id}.{row_id}", schema=SCHEMA
  row_data = bigquery.Row(SCHEMA)
  return row_data


# Store the projects in a list
projects = [project.project_id for project in list_projects()]
# Set the default project
selected_project = projects[0]
# Store the Datasets in a list
datasets = [dataset.dataset_id for dataset in list_datasets()]
# Set the default dataset
selected_dataset = datasets[0]
# Store the Tables in a list
tables = [table.table_id for table in list_tables( selected_dataset, selected_project)]
# Set the default table
selected_table = tables[0]
# Store the rows in a list
rows = [row for row in list_rows( selected_dataset, selected_project, selected_table)]
selected_row = rows[0]
# Store the Schema
SCHEMA = get_schema( selected_dataset, selected_project, selected_table, selected_row)

print(selected_row)























def get_id_full(project_id=selected_project, dataset_id=selected_dataset, table_id=selected_table):
    if project_id == "":
        selected_project = projects[0].project_id
    elif dataset_id == "":
        selected_dataset = "{}.{}".format(selected_project, selected_dataset)
    elif table_id == "":
        selected_table = "{}.{}.{}".format(selected_project, selected_dataset, selected_table)
    else:
      print("No ID selected")
    return selected_dataset, selected_project, selected_table


















print("Listing datasets in project: {}".format(selected_project))
print("Selected dataset: {}".format(selected_dataset))
print("Selected table: {}".format(selected_table))


