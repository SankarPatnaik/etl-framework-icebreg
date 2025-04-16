from core.config_loader import load_config
from core.etl_runner import run_etl_job
import sys
import logging

logging.basicConfig(filename='logs/etl.log', level=logging.INFO)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <job_name>")
        return

    job_name = sys.argv[1]
    config = load_config("config/etl_config.yaml")
    job_config = next((job for job in config['jobs'] if job['name'] == job_name), None)

    if not job_config:
        logging.error(f"Job config not found: {job_name}")
        print(f"Job config not found: {job_name}")
        return

    run_etl_job(job_config)

if __name__ == '__main__':
    main()
