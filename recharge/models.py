from django.db import models

# Create your models here.

PAYMENT_TYPE = (
    ("Cash", "Cash"),
    ("Card", "Card"),
    ("UPI", "UPI"),
)


class Recharge(models.Model):
	user = models.ForeignKey('user.User', on_delete=models.PROTECT)
	plan = models.ForeignKey('plans.Plan', on_delete=models.PROTECT)
	payment_method = models.CharField(max_length=20, choices=PAYMENT_TYPE)
	amount = models.PositiveIntegerField()
	recharge_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user)