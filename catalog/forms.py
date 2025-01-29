"""
Формы для ввода данных.
"""

from django import forms

from catalog.models import Category, Product


class CategoryForm(forms.ModelForm):
    """Форма для ввода данных о категории товаров."""
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            "name": "Наименование категории",
            "description": "Описание",
        }

    def __init__(self, *args, **kwargs):
        """Стилизация формы добавления категории."""
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": "form-control",
                    "placeholder": self.fields[field].label,
                    "style": "font-size: 0.9em; width: 100%",
                }
            )
        

class ProductForm(forms.ModelForm):
    """
    Форма для ввода данных о продукте.
    """

    class Meta:
        model = Product
        fields = "__all__"
        labels = {
            "name": "Название",
            "description": "Описание",
            "price": "Цена",
            "category": "Категория",
            "image": "Изображение",
        }

    def __init__(self, *args, **kwargs):
        """Стилизация формы добавления товара."""
        super(ProductForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": "form-control",
                    "placeholder": self.fields[field].label,
                    "style": "font-size: 0.9em; width: 100%",
                }
            )
