from product.models import Client, MovieRental

class ClientServices:
    def get_clients(self):
        clients = Client.objects.all()
        return clients
    
    def get_client_by_id(self, client_id):
        client = Client.objects.filter(id=client_id).first()
        return client
    
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
    
    # TODO: FIX THIS ERROR
    def client_rent_movie(self, rent_data):
        print("=================", rent_data, "===================")
        MovieRental.objects.create(
            rented_at=rent_data['rented_at'],
            movie=rent_data['movie_id'],
            client=rent_data['client_id'],
            price=rent_data['price'],
            payment_type=rent_data['payment_type']
        )


