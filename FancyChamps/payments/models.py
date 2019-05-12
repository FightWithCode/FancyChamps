from django.db import models


class TransactionDetail(models.Model):
    transaction_id = models.CharField(max_length=255,unique=True)
    transaction_amt = models.IntegerField(default=0)
    transaction_status = models.CharField(max_length=25)
    transact_user = models.CharField(max_length=64)
    transaction_time = models.DateTimeField(auto_now=True)
    captured = models.BooleanField(default=False)
    added_to_user = models.BooleanField(default=False)

    def __str__(self):
        return self.transaction_id


class TransactionFailedDetail(models.Model):
    transaction_id = models.CharField(max_length=255)
    transaction_amt = models.IntegerField(default=0)
    transaction_status = models.CharField(max_length=25)
    transact_user = models.CharField(max_length=64)
    transaction_time = models.DateTimeField(auto_now=True)
    captured = models.BooleanField(default=False)

    def __str__(self):
        return self.transaction_id

class PreTransData(models.Model):
    mid = models.CharField(max_length=255)
    order_id = models.CharField(max_length=64)
    url_called = models.CharField(max_length=25)
    transact_user = models.CharField(max_length=64)
    checksum = models.CharField(max_length=128)
    def __str__(self):
        return self.order_id


class WidhdrawRequest(models.Model):
    user = models.CharField(max_length=255)
    widhdraw_amount = models.CharField(max_length=64)
    request_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
