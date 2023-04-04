# type: ignore
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Facundo", surname="Maidana", url="https://facundo.dev", age=21),
              User(id=2, name="Kiki", surname="Dev",
                   url="https://mouredev.com", age=23),
              User(id=3, name="Joaquin", surname="Dadario", url="https://caco.ar", age=34)]


@router.get("/usersjson")
async def usersjson():
    return [{"name": "Facundo", "surname": "Maidana", "url": "https://facundo.dev"},
            {"name": "Kiki", "surname": "Dev", "url": "https://mouredev.com"},
            {"name": "Joaquin", "surname": "Dadario", "url": "https://caco.ar"}
            ]


@router.get("/users")
async def users():
    return users_list

# Path


@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# Query

@router.get("/user/")
async def user(id: int):
    return search_user(id)

# añadir nuevo usuario


@router.post("/user", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="El usuario ya existe")
        # raise sirve para lanzar errores o excepciones. No solo retorna el error como return
    users_list.routerend(user)
    return user


@router.put("/user")
async def user(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    return user


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se haf encontrado el usuario"}


@router.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario"}
# inicia el server : uvicorn users:router --reload
