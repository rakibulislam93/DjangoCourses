from django.db import models
from accounts.models import UserBankAccount
from .constrant import TRANSACTION_TYPE
# Create your models here.


class TransactionsModel(models.Model):
    account = models.ForeignKey(UserBankAccount,related_name='transactions',on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12,decimal_places=2)
    balance_after_transactions = models.DecimalField(max_digits=12,decimal_places=2)
    transactions_type = models.IntegerField(choices=TRANSACTION_TYPE,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']