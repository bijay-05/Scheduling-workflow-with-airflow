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

## For installing apache-airflow in local
Create a virtual env with pipenv. 
```
$pipenv --python=NON_SYSTEM_PYTHON_PATH
$pipenv shell # activate venv
$pipenv install apache-airflow
$pipenv lock # to create pipfile.lock
```

### Few pipenv commands
```
$pipenv -h #to see help
$pipenv --venv #venv info
$pipenv --py #py interpreter info
$pipenv --rm #remove venv from venv dir
$pipenv requirements
$pipenv verify # very hash in Pipfile.lock is up-to-date
$pipenv update #runs lock, then sync
$pipenv sync #install all pacs in Pipfile.lock
```

### Installing python dependencies to airflow docker container

We will accomplish this by extending the airflow image.
Create a docker file in the same directory with docker-compose.yaml and run the command
```
$docker build . --tag extended_airflow:latest
```
Then update the airflow image reference in docker-compose.yaml

Sometimes the above solution may not work, and dags may show import module error.
In such case, access the container running airflow scheduler with following
```
$docker exec -it scheduler_container_id
scheduler_container_id$pip install billboard
```