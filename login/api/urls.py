from rest_framework.routers import DefaultRouter
from login.api.views import clienteProfileViewSet

router = DefaultRouter()
router.register('cliente', clienteProfileViewSet, basename='cliente')

urlpatterns = router.urls