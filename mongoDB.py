import pymongo

client = pymongo.MongoClient("mongodb+srv://jai2355:1234@cluster0.efchi54.mongodb.net/?retryWrites=true&w=majority")
db = client.test
jk={
  {"name":"jayakumar"},
 {
  "brand": "Ford",
  "model": "Mustang",
  "years": "1964"
},{
  "brand": "Ford",
  "model": "Mustang",
  "year": "1464"}
,
    {"brand": "Ford",
  "model": "Mustang",
  "yearss": "1364"}
}
database=client["name_database"]
collection=database["name_of_tabel_or data"]
collection.insert_one(jk)