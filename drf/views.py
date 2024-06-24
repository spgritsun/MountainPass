# Create your views here.
from rest_framework import viewsets
from drf.serializers import PassSerializer
from main.models import Pass


class PassViewSet(viewsets.ModelViewSet):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer

    def get_queryset(self):
        queryset = self.queryset
        email = self.request.query_params.get('email', None)
        if email is not None:
            email = email.rstrip('/')
            queryset = Pass.objects.filter(user__email=email)
        return queryset
