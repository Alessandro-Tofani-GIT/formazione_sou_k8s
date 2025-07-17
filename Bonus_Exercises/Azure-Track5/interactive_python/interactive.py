import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient


credential = DefaultAzureCredential()

load_dotenv()
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")


client = ResourceManagementClient(credential, subscription_id)

# Test: elenco dei gruppi di risorse
for rg in client.resource_groups.list():
    print(rg.name)