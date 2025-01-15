import sender_stand_request
import data

#Funcion que copia el KIT_BODY_DATA del archivo data y lo asigna a CURRENT_BODY, luego cambia el parametro CURRENT_BODY["NAME"]
#y se le asigna el que se pase por parametro al llamar a la funcion GET_KIT_BODY_DATA("NOMBRE A PROBAR").
def get_kit_body_data(test_name):
    current_body = data.kit_body_data.copy()
    current_body['name'] = test_name
    return current_body

def get_user_token():
    user_body = data.new_user_body
    token_response = sender_stand_request.post_new_user(user_body)
    return token_response.json()['authToken']


def positive_assert(test_name):
    #kit_body = get_kit_body_data(test_name)
    positive_kit_response = sender_stand_request.post_create_new_kit(test_name,get_user_token())
    assert positive_kit_response.status_code == 201
    assert positive_kit_response.json()["name"] == test_name["name"]

def negative_assert(test_name):
    #kit_body = get_kit_body_data(test_name)
    negative_kit_response = sender_stand_request.post_create_new_kit(test_name, get_user_token())
    assert negative_kit_response.status_code == 400

#Prueba #1, Revisar que un KIT se cree con el
def test_1_create_kit_1_letter_in_name():
    new_kit_body = get_kit_body_data(data.test_1)
    positive_assert(new_kit_body)

def test_2_create_kit_511_letters_in_name():
    new_kit_body = get_kit_body_data(data.test_2)
    positive_assert(new_kit_body)

def test_3_create_kit_without_name():#El kit es creado sin nombre por lo que en este caso hay error.
    new_kit_body = get_kit_body_data(data.test_3)
    negative_assert(new_kit_body)
    
def test_4_create_kit_512_letters_in_name():#El kit es creado con un nombre con 512 caracteres por lo que en este caso hay error.
    new_kit_body = get_kit_body_data(data.test_4)
    negative_assert(new_kit_body)

def test_5_create_kit_letter_and_symbols_in_name():
    new_kit_body = get_kit_body_data(data.test_5)
    positive_assert(new_kit_body)

def test_6_create_kit_with_spaces_in_name():
    new_kit_body = get_kit_body_data(data.test_6)
    positive_assert(new_kit_body)

def test_7_create_kit_with_numbers_as_text_in_name():
    new_kit_body = get_kit_body_data(data.test_7)
    positive_assert(new_kit_body)

def test_8_create_kit_without_parameters_in_name():
    new_kit_body = {}
    negative_assert(new_kit_body)

def test_9_create_kit_with_numbers_in_name(): #El kit es creado con un nombre con 512 caracteres por lo que en este caso hay error.
    new_kit_body = get_kit_body_data(data.test_9)
    negative_assert(new_kit_body)