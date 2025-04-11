from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse
from .models import Transaction, Status, TransactionType, Category, SubCategory
from .forms import (
    TransactionForm, 
    StatusForm, TransactionTypeForm, 
    CategoryForm, SubCategoryForm
)

# -------------------------------------------------------------------------------------------------------------------------\
#     СПИСОК и ФИЛЬТРАЦИЯ
# ------------------------------------------------------------------------------------------------------------------------\
def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-date')
    
    # Фильтрация
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    status_id = request.GET.get('status')
    type_id = request.GET.get('type')
    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')
    
    if date_from:
        transactions = transactions.filter(date__gte=date_from)
    if date_to:
        transactions = transactions.filter(date__lte=date_to)
    if status_id and status_id.isdigit():
        transactions = transactions.filter(status_id=status_id)
    if type_id and type_id.isdigit():
        transactions = transactions.filter(transaction_type_id=type_id)
    if category_id and category_id.isdigit():
        transactions = transactions.filter(category_id=category_id)
    if subcategory_id and subcategory_id.isdigit():
        transactions = transactions.filter(subcategory_id=subcategory_id)
    
    # Для формирования выпадающих списков фильтра
    statuses = Status.objects.all()
    types = TransactionType.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    
    context = {
        'transactions': transactions,
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
        'filters': {
            'date_from': date_from,
            'date_to': date_to,
            'status': status_id,
            'type': type_id,
            'category': category_id,
            'subcategory': subcategory_id,
        }
    }
    return render(request, 'dds_list.html', context)


# ------------------------------------------------------------------------------------------------------------------------->
#     СОЗДАНИЕ / РЕДАКТ
# ------------------------------------------------------------------------------------------------------------------------->
def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dds:transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'dds_form.html', {'form': form, 'title': 'Создание записи'})


def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('dds:transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'dds_form.html', {'form': form, 'title': 'Редактирование записи'})


# -------------------------------------------------------------------------------------------------------------------------\
#     УДАЛЕНИЕ
# -------------------------------------------------------------------------------------------------------------------------\
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('dds:transaction_list')
    return render(request, 'dds_form.html', {
        'transaction': transaction, 
        'delete_confirm': True,
        'title': 'Удаление записи'
    })


# ------------------------------------------------------------------------------------------------------------------------->
# СПРАВОЧНИКИ Status, Type, Category, SubCategory
# ------------------------------------------------------------------------------------------------------------------------->
def refs_list(request):
    # Показываем списки всех доступных справочников
    statuses = Status.objects.all()
    types = TransactionType.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    return render(request, 'refs_list.html', {
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
    })


# ----- STATUS ----------------------------------------------------------------------------------------------\
def status_create(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dds:refs_list')
    else:
        form = StatusForm()
    return render(request, 'refs_form.html', {'form': form, 'title': 'Новый статус'})


def status_edit(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('dds:refs_list')
    else:
        form = StatusForm(instance=status)
    return render(request, 'refs_form.html', {'form': form, 'title': 'Редактирование статуса'})


def status_delete(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        status.delete()
        return redirect('dds:refs_list')
    return render(request, 'refs_form.html', {'object': status, 'delete_confirm': True, 'title': 'Удаление статуса'})


# ----- TRANSACTION TYPE ---------------------------------------------------------------------------------------------->
def ttype_create(request):
    if request.method == 'POST':
        form = TransactionTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dds:refs_list')
    else:
        form = TransactionTypeForm()
    return render(request, 'refs_form.html', {'form': form, 'title': 'Новый тип'})


def ttype_edit(request, pk):
    ttype = get_object_or_404(TransactionType, pk=pk)
    if request.method == 'POST':
        form = TransactionTypeForm(request.POST, instance=ttype)
        if form.is_valid():
            form.save()
            return redirect('dds:refs_list')
    else:
        form = TransactionTypeForm(instance=ttype)
    return render(request, 'refs_form.html', {'form': form, 'title': 'Редактирование типа'})


def ttype_delete(request, pk):
    ttype = get_object_or_404(TransactionType, pk=pk)
    if request.method == 'POST':
        ttype.delete()
        return redirect('dds:refs_list')
    return render(request, 'refs_form.html', {'object': ttype, 'delete_confirm': True, 'title': 'Удаление типа'})


# ----- CATEGORY ----------------------------------------------------------------------------------------------\
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dds:refs_list')
    else:
        form = CategoryForm()
    return render(request, 'refs_form.html', {'form': form, 'title': 'Новая категория'})


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dds:refs_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'refs_form.html', {'form': form, 'title': 'Редактирование категории'})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('dds:refs_list')
    return render(request, 'refs_form.html', {'object': category, 'delete_confirm': True, 'title': 'Удаление категории'})


# ----- SUBCATEGORY ---------------------------------------------------------------------------------------------->
def subcategory_create(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dds:refs_list')
    else:
        form = SubCategoryForm()
    return render(request, 'refs_form.html', {'form': form, 'title': 'Новая подкатегория'})


def subcategory_edit(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('dds:refs_list')
    else:
        form = SubCategoryForm(instance=subcategory)
    return render(request, 'refs_form.html', {'form': form, 'title': 'Редактирование подкатегории'})


def subcategory_delete(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    if request.method == 'POST':
        subcategory.delete()
        return redirect('dds:refs_list')
    return render(request, 'refs_form.html', {'object': subcategory, 'delete_confirm': True, 'title': 'Удаление подкатегории'})
