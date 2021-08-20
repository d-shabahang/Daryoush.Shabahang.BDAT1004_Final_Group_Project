# import packages and modules
# please note: if the app is running, then the API will automatically update
from pymongo import MongoClient
import requests as requests
import time

# connect to the MongoDB Atlas cluster with our own unique connection string
try:
    client = MongoClient(
        "mongodb+srv://daryoush:mongo1234gc@cluster0.z6kfy.mongodb.net/BDAT1004_Final_Project_API?retryWrites=true&w=majority")
    db = client.get_database('BDAT1004_Final_Project_API')
    collection = db["BDAT1004_Exchange_Rate"]

except:
    print("error ocurred")

finally:
    client.close()
    print("Connection is closed")

# loop to load data from the API to the database
while True:
    r = requests.get("https://api.exchangerate.host/latest?base=CAD")
    if r.status_code == 200:
        data = r.json()
        result = db.BDAT1004_Exchange_Rate.insert_one(data)
        print(data)
        time.sleep(60)

else:
    exit()
