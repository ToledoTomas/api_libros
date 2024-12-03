from motor.motor_asyncio import AsyncIOMotorClient
from models import Books
from bson import ObjectId

client = AsyncIOMotorClient('mongodb://localhost')

database = client.librosdb
collection = database.libros

async def get_one_book_id(id):
    book = collection.find_one({'_id':ObjectId(id)})
    return book

async def get_one_book(title):
    book = collection.find_one({'title':title})
    return book

async def get_all_books():
    books = []
    cursor = collection.find({})
    async for document in cursor:
        books.append(Books(**document))
    return books

async def create_book(book):
    new_book = await collection.insert_one(book)
    created_book = await collection.find_one({'_id': new_book.inserted_id})
    return created_book
    
async def update_book(id:str, data):
    book = {k:v for k, v in data.dict().items() if v is not None}
    await collection.update_one({'id':ObjectId(id)}, {'$set':book})
    document = await collection.find_one({'_id': ObjectId(id)})
    return document

async def delete_book(id):
    await collection.delete_one({'_id':ObjectId(id)})
    return True