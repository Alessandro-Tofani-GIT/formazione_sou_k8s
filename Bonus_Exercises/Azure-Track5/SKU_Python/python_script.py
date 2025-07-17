from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import SubscriptionClient
from azure.mgmt.resource import ResourceManagementClient

# load environment variables
load_dotenv(".env")


# Acquire a credential object
token_credential = DefaultAzureCredential()

credentials = token_credential

sub_client = SubscriptionClient(credential=credentials)

print({
  sub.display_name : sub.subscription_id
  for sub in sub_client.subscriptions.list()
})

# Acquire a credential object.
credential = token_credential

subscription_id = "af5bfaa9-a70c-4e54-bf2f-ad1a7ab27733"

# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential, subscription_id)


# Retrieve the list of resource groups
group_list = resource_client.resource_groups.list()


for group in list(group_list):
    print(group.name)
    resource_group_name = "formazione-sou-cloud"

resource_client = ResourceManagementClient(credential, subscription_id)

resource_list = resource_client.resources.list_by_resource_group(resource_group_name)

for resource in list(resource_list):
    print(resource.name)



