from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register(r'recipes', views.RecipeViewSet)

urlpatterns = router.urls
