# from keycloak import KeycloakOpenID

# class login:

#     __keycloak_openid = None
#     __config_well_know = None
#     __token = ""

#     def __init__(self, url="http://localhost:8080/admin", clientid="cc_cliente", realm="cc_realm", cliente_secret=""):
#         __keycloak_openid = KeycloakOpenID(server_url=url, client_id=clientid, realm_name=realm, client_secret_key=cliente_secret)
    
#     def obtener_well_known(self):
#         __config_well_know = self.__keycloak_openid.well_know()
    
#     def obtener_token(self):
#         __token = self.__keycloak_openid.token("user", "password")

#     def refrescar_token(self):
#         __token = self.__keycloak_openid.refresh_token(self.__token['refresh_token'])

#     def logout(self):
#         self.__keycloak_openid.logout(self.__token['refresh_token'])