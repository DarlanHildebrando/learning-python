from rest_framework import viewsets, permissions
from .serializers import SerializerClientView
from .models import Cliente

class ClientView(viewsets.ModelViewSet):
    queryset = Cliente.objects.select_related('user')

    serializer_class = SerializerClientView

    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        
        return super().get_permissions()
    


# class RegisterClient(CreateAPIView):
#     queryset = Cliente.objects.all()
#     serializer_class = serializerRegisterUser

# class ListClient(ListAPIView):
#     queryset=Cliente.objects.all()
#     serializer_class= serializerListAllClients
