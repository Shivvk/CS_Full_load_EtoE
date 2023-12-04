# Databricks notebook source
#https://docs.databricks.com/en/storage/azure-storage.html

# COMMAND ----------

#Template of spark properties to configure Azure credentials to access Azure storage
fs.azure.account.auth.type.<storage-account>.dfs.core.windows.net OAuth
fs.azure.account.oauth.provider.type.<storage-account>.dfs.core.windows.net org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider
fs.azure.account.oauth2.client.id.<storage-account>.dfs.core.windows.net <application-id>
fs.azure.account.oauth2.client.secret.<storage-account>.dfs.core.windows.net {{secrets/<secret-scope>/<service-credential-key>}}
fs.azure.account.oauth2.client.endpoint.<storage-account>.dfs.core.windows.net https://login.microsoftonline.com/<directory-id>/oauth2/token

# COMMAND ----------

#Template updated with SPN details (Please use your respective SPN credentials and storage account name)
fs.azure.account.auth.type.csadlsgen2storagedev.dfs.core.windows.net OAuth
fs.azure.account.oauth.provider.type.csadlsgen2storagedev.dfs.core.windows.net org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider
fs.azure.account.oauth2.client.id.csadlsgen2storagedev.dfs.core.windows.net 66b21694-67f0-4acb-8c7b-17c2c6e6c152
fs.azure.account.oauth2.client.secret.csadlsgen2storagedev.dfs.core.windows.net 98w8Q~s9jQ2XLO61d0g99KEg0Z4RAlPmL25W9bHp
fs.azure.account.oauth2.client.endpoint.csadlsgen2storagedev.dfs.core.windows.net https://login.microsoftonline.com/1b44d57e-6694-4d01-8c73-5fc8e058fd88/oauth2/token
