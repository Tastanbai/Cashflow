from django.contrib import admin
from .models import Status, TransactionType, Category, SubCategory, Transaction

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'transaction_type')
    search_fields = ('name',)
    list_filter = ('transaction_type',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'status', 'transaction_type', 'category', 'subcategory', 'amount')
    list_filter = ('status', 'transaction_type', 'category', 'subcategory', 'date')
    search_fields = ('comment',)
