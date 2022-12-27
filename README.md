# Scheduling-workflow-with-airflow

## Airflow with Docker-compose
The provided docker-compose.yaml file contains necessary configuration to run various components of airflow locally. This yaml file is modified 
from the one available on apache airflow website.
> Creating directories for airflow
```
$mkdir dags logs plugins

# for linux users, below command is must
$echo -e AIRFLOW_UID=$(id -u) > .env

# initialize the database
$docker-compose up airflow-init

# run the services in detached mode
$docker-compose up -d
```

