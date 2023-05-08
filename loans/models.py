from django.db import models
from django.dispatch import receiver
from django.contrib import messages
from copies.models import Copy
from users.models import Users
from datetime import datetime, timedelta
from django.db.models.signals import post_save


class Loan(models.Model):
    date_loan = models.DateTimeField(auto_now_add=True)
    date_return = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if self.date_loan and not self.date_return:
            period = self.copy.period_loan
            self.date_return = self.date_loan + timedelta(days=period)
        super().save(*args, **kwargs)


@receiver(post_save, sender=Loan)
def set_user_bloked(sender, instance, created, **kwargs):
    if created:
        if instance.user.blocked:
            return
        if instance.date_return and datetime.now() > instance.date_return:
            instance.user.blocked = True
            instance.user.save()
            messages.error(
                instance.user, 
                f"Você foi bloqueado por atraso na devolução do livro {instance.copy.title}."
            )
