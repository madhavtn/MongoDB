from pymongo import MongoClient


# MongoDB connection string
conn_string = "mongodb+srv://madhavtn95:Password@cluster0.hvtbr80.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(conn_string)

# Select the database
db = client['madhav_db']

# Select the collection
collection = db['airbnb_reviews']

# Insert a document
# insert_result = collection.insert_one({'name': 'John Doe', 'age': 30})
# print(f"Document inserted with id: {insert_result.inserted_id}")

# Query the collection

#for doc in collection.find({'room_type':'Private room'}):
#    print(doc)
find_query = {'property_type' : 'Apartment', 'room_type': 'Private room'}
for doc in collection.find(find_query):
    print(doc)
# find_query = { '$or' : [ {'property_type' : 'House'} , {'property_type' : 'Apartment'} ] }

# find_query = { 'room_type': 'Private room', '$or' : [ {'property_type' : 'House'} , {'property_type' : 'Apartment'} ] }

# find_query = { 'accommodates': { '$gt' : 2} }

#count_results = collection.count_documents(find_query)
#print("Total Documents Found : ",count_results)

#find_results = collection.find(find_query)
# for doc in find_results:
#     print(doc)

#
# grp1 = [
#     {"$group": {
#         "_id": "$address.country",  # Field to group by
#         "avg_price": {"$avg": "$price"}  # Field to avg
#     }}
# ]

# "avg_price": {"$avg": "$price"} 

# print(result)


# Close the connection
client.close()