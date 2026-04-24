from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API Usuarios y Libros")

usuarios_db = []
libros_db = []

class Usuario(BaseModel):
    id: int
    nombre: str
    email: str

class Libro(BaseModel):
    id: int
    titulo: str
    autor: str
    usuario_id: int

#CRUD DE USUARIOS

# Create
@app.post("/usuarios/", response_model=Usuario)
def crear_usuario(usuario: Usuario):
    usuarios_db.append(usuario)
    return usuario

# Read
@app.get("/usuarios/", response_model=List[Usuario])
def leer_usuarios():
    return usuarios_db

# Update
@app.put("/usuarios/{usuario_id}", response_model=Usuario)
def actualizar_usuario(usuario_id: int, usuario_actualizado: Usuario):
    for index, usuario in enumerate(usuarios_db):
        if usuario.id == usuario_id:
            usuarios_db[index] = usuario_actualizado
            return usuario_actualizado
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Delete
@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    for index, usuario in enumerate(usuarios_db):
        if usuario.id == usuario_id:
            del usuarios_db[index]
            return {"mensaje": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


#CRUD DE LIBROS

# Create
@app.post("/libros/", response_model=Libro)
def crear_libro(libro: Libro):
    libros_db.append(libro)
    return libro

# Read
@app.get("/libros/", response_model=List[Libro])
def leer_libros():
    return libros_db

# Update
@app.put("/libros/{libro_id}", response_model=Libro)
def actualizar_libro(libro_id: int, libro_actualizado: Libro):
    for index, libro in enumerate(libros_db):
        if libro.id == libro_id:
            libros_db[index] = libro_actualizado
            return libro_actualizado
    raise HTTPException(status_code=404, detail="Libro no encontrado")

# Delete
@app.delete("/libros/{libro_id}")
def eliminar_libro(libro_id: int):
    for index, libro in enumerate(libros_db):
        if libro.id == libro_id:
            del libros_db[index]
            return {"mensaje": "Libro eliminado"}
    raise HTTPException(status_code=404, detail="Libro no encontrado")
