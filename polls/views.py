from rest_framework.viewsets import ModelViewSet
from .models import Contribuinte, User
from .serializers import ContribuinteSerializer, UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ContribuinteViewSet(ModelViewSet):
    queryset = Contribuinte.objects.all()
    serializer_class = ContribuinteSerializer