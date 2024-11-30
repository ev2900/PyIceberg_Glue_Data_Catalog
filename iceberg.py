import os

os.environ['AWS_DEFAULT_REGION'] = "<region>"
os.environ['AWS_ACCESS_KEY_ID'] = "<access-key>"
os.environ['AWS_SECRET_ACCESS_KEY'] = "<access-key-secret>"

from pyiceberg.catalog import load_catalog

#
# 1. Manipulate Glue catalog
#

# List Glue data catalogs
catalog = load_catalog("glue", **{"type": "glue"})

print(catalog.list_namespaces())

# List Glue tables in the database
print(catalog.list_tables('iceberg'))

# List table metadata
print(table.metadata)


#
# 2. Read iceberg table
#

table = catalog.load_table("iceberg.sampledataicebergtable")

scan = table.scan()

#scan = scan.to_arrow()
scan = scan.to_pandas()

#print(scan)

#
# 3. Write iceberg table
#

import pyarrow as pa

df = pa.Table.from_pylist(
    [
        {"id": "7", "name": "Jim", "create_date": "2020-01-01"},
        {"id": "8", "name": "Anna", "create_date": "2020-01-01"} 
    ],
)

table.append(df)
# table.overwrite(df)

#
# Paritioning  
#

# Check that the write was sucssful 
scan = table.scan()

#scan = scan.to_arrow()
scan = scan.to_pandas()

print(scan)
