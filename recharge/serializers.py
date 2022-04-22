from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from recharge.models import Recharge
from plans.models import Plan
from plans.serializers import PlanSrerializer



class RechargeSrerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recharge
        fields = '__all__'


class RechargeHistorySrerializer(serializers.ModelSerializer):
    transaction_id = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Recharge
        fields = ['transaction_id', 'user', 'plan', 'payment_method', 'amount', 'recharge_date' ]


    def get_transaction_id(self,obj):
        return obj.id

   