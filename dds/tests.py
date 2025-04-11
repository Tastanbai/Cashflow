from django.test import TestCase
from django.urls import reverse
from .models import TransactionType, Category, SubCategory, Status, Transaction
from django.utils import timezone

class DDSTestCase(TestCase):
    def setUp(self):
        # Создадим тестовые данные
        self.status = Status.objects.create(name="Бизнес")
        self.transaction_type = TransactionType.objects.create(name="Пополнение")
        self.category = Category.objects.create(name="Маркетинг", transaction_type=self.transaction_type)
        self.subcategory = SubCategory.objects.create(name="Avito", category=self.category)

    def test_create_transaction(self):
        # Создание транзакции через модель
        transaction = Transaction.objects.create(
            date=timezone.now(),
            status=self.status,
            transaction_type=self.transaction_type,
            category=self.category,
            subcategory=self.subcategory,
            amount=1000.00,
            comment="Тестовая транзакция"
        )
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(transaction.amount, 1000.00)
