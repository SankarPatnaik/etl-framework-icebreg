# Generic ETL Framework with Apache Iceberg & Python

This ETL framework is designed to extract data from 100+ sources, transform using Pandas/Arrow, and load into Apache Iceberg format on AWS S3.

## 🔧 Features
- Source connectors: MySQL, Oracle, SQL Server, MongoDB, .dat files
- Modular, config-driven pipeline
- Pandas → Arrow → Iceberg on S3
- Prefect-based orchestration

## 🛠️ Usage
```bash
python main.py mysql_customers
```

Or trigger via Prefect UI/CLI:
```bash
prefect deployment build flows/etl_flow.py:etl_flow -n etl-deployment
prefect deployment apply etl_flow-deployment.yaml
prefect agent start
```

## 📁 Config Example (YAML)
See `config/etl_config.yaml`

## 🔐 Environment
Define AWS creds in `.env` file or via environment variables
