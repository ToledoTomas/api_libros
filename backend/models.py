from pydantic import BaseModel

class Libros(BaseModel):
    id
    titulo: str
    autor: str
    pagina: int
    completado: bool = False