from fastapi import FastAPI, HTTPException
from database import get_all_books, create_book, get_one_book, get_one_book_id, delete_book, update_book
from models import Books, UpdateBooks

app = FastAPI()


@app.get('/api/books')
async def get_books():
    books = await get_all_books()
    return books

@app.get('/api/books/{id}', response_model=Books)
async def get_book(id:str):
    response = await get_one_book_id(id)
    if response:
        return response
    raise HTTPException(400,f'No se encuentra el libro con id: {id}')

@app.post('/api/books', response_model=Books)
async def create_books(book:Books):
    
    bookFound = await get_one_book(book.title)
    if bookFound:
        raise HTTPException(409, 'Este libro ya existe')
    
    response = await create_book(book.dict())
    if response:
        return response
    raise HTTPException(400,'Algo salió mal')

@app.put('/api/books/{id}', response_model=Books)
async def update_books(id: str, book: UpdateBooks):
    response = await update_book(id, book.dict())
    if response:
        return response
    return HTTPException(404, f'Libro con id: {id} no encontrado')

@app.delete('/api/books/{id}')
async def delete_books(id:str):
    response = await delete_book(id)
    if response:
        return 'Libro eliminado con exito'
    raise HTTPException(404, f'Libro con id: {id} no encontrado')