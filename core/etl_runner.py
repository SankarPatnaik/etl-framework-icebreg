from connectors import sql_server, oracle, mysql, mongodb, datfile
from core.s3_iceberg_writer import write_to_s3_iceberg
import logging

def run_etl_job(job_config):
    source = job_config['source']
    target = job_config['target']

    connector_map = {
        'sql_server': sql_server,
        'oracle': oracle,
        'mysql': mysql,
        'mongodb': mongodb,
        'dat': datfile
    }

    connector = connector_map[source['type']]
    df = connector.read(source)

    write_to_s3_iceberg(df, target)
