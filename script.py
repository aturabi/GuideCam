from google.cloud import datastore

client = datastore.Client()
product_key = client.key('Product', 123)
print(client.get(product_key))
