from pymongo.mongo_client import MongoClient
import ssl
import os

# Get credentials from environment variables

user = os.environ.get("MONGODB_CARLO_USER")
password = os.environ.get("MONGODB_CARLO_PASSWORD")
cluster = os.environ.get("MONGODB_CARLO_CLUSTER")


uri = f"mongodb+srv://{user}:{password}@{cluster}/?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=true"

# Create a new client and connect to the server
client = MongoClient(uri, tls=True, tlsAllowInvalidCertificates=True)

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# Connect to collection
db = client["carlo"].houses
