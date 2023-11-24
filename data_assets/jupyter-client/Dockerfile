FROM jupyter/datascience-notebook
    
USER root

RUN apt-get update && apt-get -y install libpq-dev gcc  && pip install psycopg2

#USER $NB_UID
# SQL magic
#RUN pip install sql_magic

# Postgres
#RUN pip install psycopg2-binary