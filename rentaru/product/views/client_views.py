from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from product.serializers import *
from product.selectors import *


class ClientListAPIView(APIView):
    permission_classes = []

    def get(self, request):
        clients = get_clients()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ClientForCreateSerializer, responses={201: ClientSerializer()})
    def post(self, request):
        name = request.data.get('name', '')
        cpf = request.data.get('cpf', '')
        new_client = create_client(name, cpf)
        if new_client:
            serializer = ClientSerializer(new_client)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Erro ao criar cliente'}, status=status.HTTP_400_BAD_REQUEST)

class ClientDetailAPIView(APIView):
    permission_classes = []

    def delete(self, request, client_id):
        deleted = delete_client(client_id)
        if deleted:
            return Response({'message': 'Cliente excluído com sucesso'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'Cliente não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=ClientForCreateSerializer, responses={201: ClientSerializer()})
    def put(self, request, client_id):
        new_name = request.data.get('name', '')
        new_cpf = request.data.get('cpf', '')
        updated_client = update_client(client_id, new_name, new_cpf)
        if updated_client:
            serializer = ClientSerializer(updated_client)
            return Response(serializer.data)
        else:
            return Response({'message': 'Cliente não encontrado'}, status=status.HTTP_404_NOT_FOUND)
