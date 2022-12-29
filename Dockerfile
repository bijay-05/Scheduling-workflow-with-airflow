FROM apache/airflow:2.5.0

COPY Pipfile Pipfile.lock /

RUN pip install --user --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy
