from django.db import models
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class TransactionType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return f"{self.name} ({self.transaction_type.name})"


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return f"{self.name} -> {self.category.name}"


class Transaction(models.Model):
    date = models.DateField(default=timezone.now)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='transactions')
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.PROTECT, related_name='transactions')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='transactions')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} | {self.transaction_type.name} | {self.amount}"
