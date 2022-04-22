from rest_framework import serializers
from plans.models import Plan


class PlanSrerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Plan
        fields = '__all__'
