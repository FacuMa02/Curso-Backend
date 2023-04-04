from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# OAuth2PasswordBearer: se encarga de gestionar la autenticación del usuario y contraseña
"""
OAuth2PasswordRequestForm: la forma en la que se enviaran los criterios de autenticación desde el cliente a
 nuestro backend."""


router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):  # herencia de user
    password: str


users_db = {
    "facuma8": {
        "username": "facuma8",
        "full_name": "Facundo Maidana",
        "email": "facumaidana2001@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "benjama5": {
        "username": "benjama5",
        "full_name": "Benjamin Maidana",
        "email": "benjamaidana@gmail.com",
        "disabled": True,
        "password": "654321"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    # los dos asteriscos indican que pueden ir un numero arbitrario de parametros


async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Credenciales de autenticación no validas.", headers={"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Usuario inactivo")
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto"
        )
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta"
        )
    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
