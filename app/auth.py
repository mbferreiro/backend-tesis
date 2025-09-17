from keycloak import KeycloakAdmin, KeycloakOpenID

#KEYCLOAK_URL = "http://localhost:8080/"
KEYCLOAK_URL = "http://keycloak:8080/"
REALM = "tesis"
CLIENT_ID = "backend"
CLIENT_SECRET = "prdcKsCPIIozuAKqMKLW2Sp9wtEkeUFT"  # pegá el valor que copiaste del panel

# Admin: crea usuarios y asigna roles
admin = KeycloakAdmin(
    server_url=KEYCLOAK_URL,
    username="admin",
    password="admin",
    realm_name="tesis",
     user_realm_name="master",
    verify=True
)

# OpenID: hace login con usuario/contraseña
openid = KeycloakOpenID(
    server_url=KEYCLOAK_URL,
    client_id=CLIENT_ID,
    realm_name=REALM,
    client_secret_key=CLIENT_SECRET,
    verify=True
)

def crear_usuario(email, username, password, rol):
    # Crear usuario
    user_id = admin.create_user({
        "email": email,
        "username": username,
        "enabled": True,
        "credentials": [{"type": "password", "value": password, "temporary": False}]
    })
    # Asignar rol
    role = admin.get_realm_role(rol)
    admin.assign_realm_roles(user_id=user_id, roles=[role])

def login(username, password):
    return openid.token(username, password)
