FROM apache/airflow:3.0.2-python3.11

COPY airflow/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir \
    -r /tmp/requirements.txt \
    --constraint https://raw.githubusercontent.com/apache/airflow/constraints-3.0.2/constraints-3.11.txt