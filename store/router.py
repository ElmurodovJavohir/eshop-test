from rest_framework import routers
from store.views import UserViewSet, ProductViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
