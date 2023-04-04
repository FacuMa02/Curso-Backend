from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)


# recursos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")


# @app.get("/")
# async def root():
#     return "Hola Mundo"

# agregar una peticion get, pero direccionado a /url


@app.get("/url")
async def root():
    return {"url_curso": "https//mouredev.com/python"}


# inicia el server : uvicorn main:app --reload