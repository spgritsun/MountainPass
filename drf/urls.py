from django.urls import path, include
from rest_framework import routers

from drf.views import PassViewSet

router = routers.SimpleRouter()
router.register(r'passes', PassViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
