from rest_framework import viewsets, permissions
from .serializers import SerializerClientView
from .models import Cliente

class ClientView(viewsets.ModelViewSet):
    queryset = Cliente.objects.select_related('user')

    serializer_class = SerializerClientView

    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        
        return super().get_permissions()
    
