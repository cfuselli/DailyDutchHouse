from mongo import db

query = {"link": None}  # Matches documents with missing "link" field

pre_result = db.find(query)

pre_result = [house for house in pre_result]

print(f"Found {len(pre_result)} documents")

for house in pre_result:
    print(f"House n: {house['house_n']}")
    print(f"Address: {house['address']}")
    print(f"City: {house['city']}")
    print(f"Price: {house['price']}")
    print(f"Status: {house['status']}")
    print(f"Details: {house['details']}")
    print(f"Link: {house['link']}")
    print(f"Images: {house['images']}")
    print(f"Date: {house['date']}")
    print()

inp = input("Do you want to delete these documents? (y/n) ")

if inp != "y":
    exit()

# Delete documents that match the query
result = db.delete_many(query)

# Print the number of documents deleted
print(f"Deleted {result.deleted_count} documents")