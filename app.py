import json
import ovh

client = ovh.Client(
    endpoint='ovh-eu',              
    application_key='9c3351c8add50664',
    application_secret='552442f4863935e6927d3dd30d204c18', 
    consumer_key='e369babea401d7c7fe23009693ede6ba',     
)
result = client.get( '/me')
# Pretty print
print(json.dumps(result, indent=4))