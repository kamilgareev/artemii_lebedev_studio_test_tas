from rest_framework.routers import SimpleRouter

from .views import SpecialistsRegistryViewSet

router = SimpleRouter()
router.register(r'specialists_registry', SpecialistsRegistryViewSet)

urlpatterns = []

urlpatterns += router.urls
