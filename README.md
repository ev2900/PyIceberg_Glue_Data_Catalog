# PyIceberg example with Glue Data Catalog

<img width="85" alt="map-user" src="https://img.shields.io/badge/views-055-green"> <img width="125" alt="map-user" src="https://img.shields.io/badge/unique visits-025-green">

[PyIceberg](https://py.iceberg.apache.org/) is a Python library that can read, write etc. to Apache Iceberg tables. 

This code sample demonstrated how PyIceberg run via. a SageMakerAI studio Juypter notebook can interact with an existing Iceberg table registered with the Glue Data Catalog.

The architecture below depicts this

<img width="700" alt="quick_setup" src="

## Example

You can test this pyIceberg with a Glue Data Catalog registered Iceberg table. Begin by deploying the CloudFormation stack below. This will create the required AWS resources.

> [!WARNING]
> The CloudFormation stack creates IAM role(s) that have ADMIN permissions. This is not appropriate for production deployments. Scope these roles down before using this CloudFormation in production.

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=pyiceberg-gdc&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/pyIceberg_gdc.yaml)

### Create a sample Iceberg table in AWS via. Glue

Navigate to the Glue console ETL jobs page, select the *Create Iceberg Table* and select the *Run* button

<img width="700" alt="quick_setup" src="https://github.com/ev2900/PyIceberg_Glue_Data_Catalog/blob/main/README/run_glue_job.png">

This will create an Iceberg table named ```sampledataicebergtable``` registered with the Glue data catalog database ```iceberg```

### Open SageMakerAI Studio

