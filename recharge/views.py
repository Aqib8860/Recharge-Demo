from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from django.core.exceptions import ObjectDoesNotExist
from recharge.serializers import RechargeSrerializer, RechargeHistorySrerializer
from user.models import User
from recharge.models import Recharge
from plans.models import Plan
from django.contrib.auth import get_user_model


User = get_user_model()



class RechargeViewSet(viewsets.ModelViewSet):
	queryset = Recharge.objects.all()
	serializer_class = RechargeSrerializer
	permission_classes = [permissions.IsAuthenticated]
	http_method_names = ['post', 'options', 'head']

	def list(self, request, *args, **kwargs):
		try:
			user = User.objects.get(id=request.user.id)
		except ObjectDoesNotExist:
			return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)

		queryset = self.queryset.filter(user=user)
		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)

		def create(self, request, *args, **kwargs):
			try:
				user = User.objects.get(id=request.user.id)
			except ObjectDoesNotExist:
				return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)

			plan = Plan.objects.filter(id=self.request.data['plan'])

			if plan.exists():
				serializer = self.get_serializer(data=request.data)
				serializer.is_valid(raise_exception=True)
				self.perform_create(serializer.save())
				return Response({"msg": "Recharge Success"}, status=200)

			else:
				return Response({"error": "Plan does not exist"}, status=400)


class RechargeHistoryViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Recharge.objects.all()
	serializer_class = RechargeHistorySrerializer
	permission_classes = [permissions.IsAuthenticated]
	http_method_names = ['get', 'options', 'head']

	def list(self, request, *args, **kwargs):
		try:
			user = User.objects.get(id=request.user.id)
		except ObjectDoesNotExist:
			return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)
		queryset = self.queryset.filter(user=user)
		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)
