from rest_framework.routers import DefaultRouter
from .views import BookView, HomeView
from django.urls import path, include

router = DefaultRouter()
router.register(r'books', BookView)

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('api/', include(router.urls)),
]