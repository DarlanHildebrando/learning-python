from rest_framework.routers import DefaultRouter
from .views import ClientView

router = DefaultRouter()

router.register(r'cliente', ClientView, basename='cliente')

urlpatterns = router.urls