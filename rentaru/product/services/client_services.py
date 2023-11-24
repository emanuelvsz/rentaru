from product.models import Client

class ClientServices:
    def get_clients(self):
        clients = Client.objects.all()
        return clients
    
    def create_client(self, name, cpf):
        new_client = Client(name=name, cpf=cpf)
        new_client.save()
        return new_client
    
    def delete_client(self, client_id):
        client = Client.objects.get(pk=client_id)
        client.delete()
        return True
    
    def update_client(self, client_id, new_name=None, new_cpf=None):
        client = Client.objects.get(id=client_id)
        if new_name:
            client.name = new_name
        if new_cpf: 
            client.cpf = new_cpf
        client.save()
        return client



