from prefect import flow, task
from core.config_loader import load_config
from core.etl_runner import run_etl_job

@task
def run_job(job_config):
    run_etl_job(job_config)

@flow(name="Generic ETL Flow")
def etl_flow():
    config = load_config("config/etl_config.yaml")
    for job in config['jobs']:
        run_job.submit(job)
