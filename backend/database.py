from motor.motor_asyncio import AsyncIOMotorClient
from models import Libros

client = AsyncIOMotorClient('mongodb://localhost')

database = client.librosdb
collection = database.libros

async def get_one_book_id(id):
    book = collection.find_one({'_id':id})
    return book

async def get_all_books():
    books = []
    cursor = collection.find()
    async for document in cursor:
        books.append(Libros(**document))
    return books

async def create_book(book):
    new_book = collection.insert_one(book)
    created_book = await collection.find_one({'_id': new_book.inserted_id})
    return created_book
    
async def update_book(id:str, book):
    await collection.update_one({'id':id}, {'$set':book})
    document = await collection.find_one({'_id': id})
    return document

async def delete_book(id):
    await collection.delete_one({'_id':id})
    return True