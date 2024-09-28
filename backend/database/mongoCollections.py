from helpers import is_valid_ingredient, is_valid_id
from datetime import date
from mongoConnection import get_database
from bson.objectid import ObjectId

# Schemas:

# ingredients {
#     name: str
#     date: date
#     quantity(?): float
# }

# recipes {
#     name: str
#     ingredients[]: arr[Obj]
#     description: str
#     rating(?): int
# }

# def get_database():
#     # connects to mhacks2024 db
#     CONNECTION_STRING = "mongodb://localhost:27017"
#     client = MongoClient(CONNECTION_STRING)
 
#     return client['mhacks2024']

def get_ingredients():
    # returns a list of all ingredient objects in ingredients collection
    
    db = get_database()
    ingredientsCollection = db['ingredients']

    res = ingredientsCollection.find()
    return res

def add_ingredient(input:dict):
    # adds a new ingredient object with parameters in input dictionary
    # input{name, Date=currentDate, quantity=None}
    # returns success or failure

    try:
        if not is_valid_ingredient(input):
            raise ValueError("invalid ingredient input")
        
        ingredientObj = {
            "name": input.name,
            "date": date.today(),
            "quantity": input.quantity if input.get('quantity') != None else 1
        }

        db = get_database()
        ingredientsCollection = db['ingredients']

        res = ingredientsCollection.insert_one(ingredientObj)

        return res
        
    except Exception as e:
        print(e)

def delete_ingredient(id: str):
    # deletes ingredient object with _id of id
    # returns success or failure

    try:
        if not is_valid_id(id):
            raise ValueError('invalid id string')
        
        db = get_database()
        ingredientsCollection = db['ingredients']

        filter={"_id": ObjectId(id)}
        res = ingredientsCollection.delete_one(filter)

        if (res.deleted_count > 0):
            print("ingredient successfully deleted")
        else:
            print("deletion failed")


    except Exception as e:
        print(e)




    return 


# res = get_ingredients()
# for items in res:
#     print(items)