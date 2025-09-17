from fastapi import APIRouter, Body, HTTPException
from app.auth import crear_usuario, login

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(data: dict = Body(...)):
    try:
        crear_usuario(data["email"], data["username"], data["password"], data["rol"])
        return {"msg": "Usuario creado"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def do_login(data: dict = Body(...)):
    try:
        return login(data["username"], data["password"])
    except:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
