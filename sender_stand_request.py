import configuration
import data
import requests

"""CREA UN NUEVO USUARIO Y MUESTRA EL CODIGO authToken"""
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def post_create_new_kit(kit_body,authtoken):
    new_headers = {
    "Content-Type": "application/json","Authorization": f'Bearer {authtoken}'
    }
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS,
                        json=kit_body,
                        headers=new_headers)