from fastapi import APIRouter
from config.db import conn
from models.userr import users
from schemas.userrr import User, Update


route = APIRouter()

@route.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()

@route.get("/{id}")
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

@route.post("/")
async def create_data(New: User):
    conn.execute(users.insert().values(
        Name=New.Name,
        email=New.email,
        password=New.password
    ))
    return conn.execute(users.select()).fetchall()

@route.put("/{id}")
async def update_data(id:int , New_Update : Update):
    conn.execute(users.update(
        Name=New_Update.Name,
        email=New_Update.email,
        password=New_Update.password
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()

@route.delete("/{id}")
async def delete_data(id:int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()