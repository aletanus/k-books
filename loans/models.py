from django.db import models

from copies.models import Copy
from users.models import Users


class Loan(models.Model):
    date_loan = models.DateTimeField(auto_now_add=True)
    date_return = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
