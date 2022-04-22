from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets
from plans.serializers import PlanSrerializer
from plans.models import Plan


class PlansViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSrerializer
