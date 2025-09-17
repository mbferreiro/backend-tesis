import os
from keycloak import KeycloakAdmin, KeycloakOpenID
from keycloak.exceptions import KeycloakGetError

KEYCLOAK_URL = os.getenv("KEYCLOAK_URL", "http://localhost:8080/")
REALM         = os.getenv("KEYCLOAK_REALM", "tesis")
CLIENT_ID     = os.getenv("KEYCLOAK_CLIENT_ID", "backend")
CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET", "")

admin = KeycloakAdmin(
    server_url=KEYCLOAK_URL,
    username=os.getenv("KEYCLOAK_ADMIN_USER", "admin"),
    password=os.getenv("KEYCLOAK_ADMIN_PASS", "admin"),
    realm_name=REALM,
    user_realm_name="master",
    verify=True,
)

# OpenID: hace login con usuario/contraseña
openid = KeycloakOpenID(
    server_url=KEYCLOAK_URL,
    client_id=CLIENT_ID,
    realm_name=REALM,
    client_secret_key=CLIENT_SECRET,
    verify=True
)

def crear_usuario(email: str, username: str, password: str, rol: str | None = None) -> str:
    
    try:
        user_id = admin.create_user({
            "email": email,
            "emailVerified": False,
            "username": username,
            "enabled": True,
            "credentials": [{"type": "password", "value": password, "temporary": False}],
            
        })
    except KeycloakGetError as e:
        # 409 = conflict (usuario/email existente)
        if getattr(e, "response_code", None) == 409:
            raise ValueError("El email o usuario ya está registrado.")
        raise

    # La librería a veces retorna dict/None; recuperar id robustamente
    if not user_id:
        user_id = admin.get_user_id(username)
    if not user_id:
        # intento por email
        users = admin.get_users(query={"email": email})
        if users:
            user_id = users[0]["id"]

    if not user_id:
        raise RuntimeError("No se pudo obtener el ID del usuario recién creado.")

    if rol:
        role = admin.get_realm_role(rol)  # nombre exacto del rol en el realm
        admin.assign_realm_roles(user_id=user_id, roles=[role])

    return user_id

def login(username, password):
    return openid.token(username, password)
