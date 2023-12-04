# Databricks notebook source
# MAGIC %sql
# MAGIC -- mysql query
# MAGIC select control.source_ref_id, control.server_name, control.port, control.database_name, control.user_name, control.secret_name, control.storage_account, control.adls_url, control.container_name, control.logic_app_url, control.email_id, param.source_file_or_table_name, param.adls_file_path, param.bronze_schema, param.bronze_tbl, param.silver_schema, param.silver_tbl, param.gold_schema, param.gold_tbl from metadata_schema.tbl_source_control as control join metadata_schema.tbl_parameters as param on control.job_id = param.job_id where param.job_id = 102

# COMMAND ----------

#mysql lookup adf
@concat('select control.source_ref_id, control.server_name, control.port, control.database_name, control.user_name, control.secret_name, control.storage_account, control.adls_url, control.container_name, control.logic_app_url, control.email_id, param.source_file_or_table_name, param.adls_file_path, param.bronze_schema, param.bronze_tbl, param.silver_schema, param.silver_tbl, param.gold_schema, param.gold_tbl from ',pipeline().parameters.metadata_database,'.tbl_source_control as control join ',pipeline().parameters.metadata_database,'.tbl_parameters as param on control.job_id = param.job_id where param.job_id = ',pipeline().parameters.job_id)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- sftp query
# MAGIC select control.source_ref_id, control.host_name, control.port, control.user_name, control.secret_name, control.storage_account, control.adls_url, control.container_name, control.logic_app_url, control.email_id, param.source_file_or_table_name, param.adls_file_path, param.bronze_schema, param.bronze_tbl, param.silver_schema, param.silver_tbl, param.gold_schema, param.gold_tbl from metadata_schema.tbl_source_control as control join metadata_schema.tbl_parameters as param on control.job_id = param.job_id where param.job_id = 101
# MAGIC

# COMMAND ----------

#sftp lookup adf
@concat('select control.source_ref_id, control.host_name, control.port, control.user_name, control.secret_name, control.storage_account, control.adls_url, control.container_name, control.logic_app_url, control.email_id, param.source_file_or_table_name, param.source_file_path, param.adls_file_path, param.bronze_schema, param.bronze_tbl, param.silver_schema, param.silver_tbl, param.gold_schema, param.gold_tbl from ', pipeline().parameters.metadata_database,'.tbl_source_control as control join ',pipeline().parameters.metadata_database,'.tbl_parameters as param on control.job_id = param.job_id where param.job_id = ',pipeline().parameters.job_id)
