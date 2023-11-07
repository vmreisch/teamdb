from rest_framework import generics, permissions
from .models import Athlete
from .serializers import AthleteSerializer
from .permissions import IsOwnerOrReadOnly 

class AthleteList(generics.ListCreateAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AthleteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [IsOwnerOrReadOnly]