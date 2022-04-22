from django.urls import path, include
from rest_framework import routers
from plans import views


router = routers.DefaultRouter()
router.register('view-add-plans', views.PlansViewSet, basename='viewaddplans')

urlpatterns = [
    path('', include(router.urls)),
]
