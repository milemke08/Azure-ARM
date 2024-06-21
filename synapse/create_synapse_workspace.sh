az synapse workspace create --name your-synapse-workspace --resource-group your-resource-group --storage-account your-storage-account --file-system your-file-system --sql-admin-login-user your-sql-admin --sql-admin-login-password your-sql-password --location eastus
az synapse sql pool create --name your-sql-pool --workspace-name your-synapse-workspace --performance-level DW100c --resource-group your-resource-group