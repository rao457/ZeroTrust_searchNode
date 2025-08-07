from rest_framework.routers import DefaultRouter
from .views import BookView
from django.urls import path, include

router = DefaultRouter()
router.register(r'books', BookView)

urlpatterns = [
    path('', include(router.urls)),
]