from pets.models import Pet
from pets.apis.serializers import PetSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


class PetApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PetSerializer
    queryset = Pet.objects.all()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_pet_by_user(request):
    pets = Pet.objects.filter(user=request.user.id)
    serializer = PetSerializer(pets, many=True)
    return Response(serializer.data)

