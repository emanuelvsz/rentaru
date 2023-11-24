from product.services import *

def get_clients():
    return ClientServices().get_clients()

def get_client_by_id(client_id):
    return ClientServices().get_client_by_id(client_id)

def create_client(name, cpf):
    return ClientServices().create_client(name, cpf)

def delete_client(client_id):
    return ClientServices().delete_client(client_id)

def update_client(client_id, new_name, new_cpf):
    return ClientServices().update_client(client_id, new_name, new_cpf)

def client_rent_movie(rent_data):
    return ClientServices().client_rent_movie(rent_data)