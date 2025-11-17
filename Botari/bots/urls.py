
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BotViewSet, ScenarioViewSet, StepViewSet

router = DefaultRouter()
router.register(r'bots', BotViewSet)
router.register(r'scenarios', ScenarioViewSet)
router.register(r'scenarios/(?P<scenario_pk>[^/.]+)/steps', StepViewSet, basename='scenario-steps')

urlpatterns = [
    path('', include(router.urls)),
]