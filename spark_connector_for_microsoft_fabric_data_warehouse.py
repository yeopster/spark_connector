# -*- coding: utf-8 -*-
"""Spark connector for Microsoft Fabric Data Warehouse

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1USeyznRDpSJowgMSrATEs5fLXJT07UtS
"""

import sempy.fabric as fabric
import com.microsoft.spark.fabric
from com.microsoft.spark.fabric.Constants import Constants

def fabric_dw_reader_writer_demo(source_table: str, destination_table: str, workspace_name: str, mode: str):
  try:
    # Resolve the workspace ID
    workspace_id = fabric.resolve_workspace_id(workspace_name)
    print(f"Workspace ID: {workspace_id}")

    # Read data from warehouse/lakehouse
    df = spark.read.option(Constants.WorkspaceId, workspace_id).synapsesql(source_table)
    print(f"Dta read from {source_table} successfully.")

    # Write data to warehouse/lakehouse
    df.write.mode(mode).option(Constants.WorkspaceId, workspace_id).synapsesql(destination_table)
    print(f"Data written to {destination_table} successfully in '{mode}' mode.")

  except Exception as e:
    print(f"An error occured: {e}")

source_table = "DataWarehouseName.SchemaName.Table1"
destination_table = "DataWarehouseName.SchemaName.Table2"
workspace_name = "test_workspace"
mode = "overwrite" #options :'errorifexists', 'ignore', 'append', 'overwrite'

fabric_dw_reader_writer_demo(source_table, destination_table, workspace_name, write_mode)