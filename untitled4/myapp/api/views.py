from rest_framework import viewsets
from .serializers import PersonSerializer
from .. import models


class PersonViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that allows users to be viewed or edited.
    """
    queryset = models.Person.objects.all()
    serializer_class = PersonSerializer

