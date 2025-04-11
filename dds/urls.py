from django.urls import path
from . import views

app_name = 'dds'

urlpatterns = [
    # Транзакции
    path('', views.transaction_list, name='transaction_list'),
    path('create/', views.transaction_create, name='transaction_create'),
    path('<int:pk>/edit/', views.transaction_edit, name='transaction_edit'),
    path('<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),
    
    # Справочники
    path('refs/', views.refs_list, name='refs_list'),
    
    # Status
    path('refs/status/create/', views.status_create, name='status_create'),
    path('refs/status/<int:pk>/edit/', views.status_edit, name='status_edit'),
    path('refs/status/<int:pk>/delete/', views.status_delete, name='status_delete'),
    
    # TransactionType
    path('refs/type/create/', views.ttype_create, name='ttype_create'),
    path('refs/type/<int:pk>/edit/', views.ttype_edit, name='ttype_edit'),
    path('refs/type/<int:pk>/delete/', views.ttype_delete, name='ttype_delete'),
    
    # Category
    path('refs/category/create/', views.category_create, name='category_create'),
    path('refs/category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('refs/category/<int:pk>/delete/', views.category_delete, name='category_delete'),
    
    # SubCategory
    path('refs/subcategory/create/', views.subcategory_create, name='subcategory_create'),
    path('refs/subcategory/<int:pk>/edit/', views.subcategory_edit, name='subcategory_edit'),
    path('refs/subcategory/<int:pk>/delete/', views.subcategory_delete, name='subcategory_delete'),
]
