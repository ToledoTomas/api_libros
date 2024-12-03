from fastapi import FastAPI

app = FastAPI()


@app.get('/api/libros')
async def get_libros():
    return 'todos los libros'

@app.get('/api/libros/{id}')
async def get_libro():
    return 'un solo libro'

@app.post('/api/libros')
async def create_libros():
    return 'crear los libros'

@app.put('/api/libros/{id}')
async def update_libros():
    return 'actualizando los libros'

@app.delete('/api/libros/{id}')
async def delete_libros():
    return 'eliminando libros'