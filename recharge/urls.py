from django.urls import path, include
from rest_framework import routers
from recharge import views


router = routers.DefaultRouter()

router.register('add-recharge', views.RechargeViewSet, basename='addrecharge')
router.register('recharge-history', views.RechargeHistoryViewSet, basename='rechargehistoryrecharge')

urlpatterns = [
    path('', include(router.urls)),
]
