from django import forms
from .models import Transaction, Status, TransactionType, Category, SubCategory

class TransactionForm(forms.ModelForm):
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Transaction
        fields = ['date', 'status', 'transaction_type', 'category', 'subcategory', 'amount', 'comment']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Сортируем поля для удобства или добавляем лейблы
        self.fields['date'].label = 'Дата'
        self.fields['status'].label = 'Статус'
        self.fields['transaction_type'].label = 'Тип'
        self.fields['category'].label = 'Категория'
        self.fields['subcategory'].label = 'Подкатегория'
        self.fields['amount'].label = 'Сумма'
        self.fields['comment'].label = 'Комментарий'
        
        # При первом открытии формы, если выбрана категория, фильтруем подкатегории
        # Если нужно динамическое обновление в реальном времени, потребуется JS/AJAX:
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.category:
            self.fields['subcategory'].queryset = self.instance.category.subcategories.all()


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TransactionTypeForm(forms.ModelForm):
    class Meta:
        model = TransactionType
        fields = ['name']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'transaction_type']


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'category']
