"""
Формы для ввода данных.
"""

import os

from dotenv import load_dotenv
from django import forms

from catalog.models import Category, Product

load_dotenv()

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
            self.fields[field].widget.attrs.update({
                    "class": "form-control",
                    "placeholder": self.fields[field].label,
                    "style": "font-size: 0.9em; width: 100%",
                })

    def clean(self):
        forbidden_words = os.getenv("FORBIDDEN_WORDS").split(",")
        cleaned_data = super().clean()

        cleaned_name = cleaned_data.get("name").split()
        for word in cleaned_name:
            if word.lower() in forbidden_words:
                self.add_error("name", "Поле с наименованием категории содержит запрещённое слово %s." % word)
                break

        cleaned_description = cleaned_data.get("description").split()
        for word in cleaned_description:
            if word.lower() in forbidden_words:
                self.add_error("description", "Поле с описанием категории содержит запрещённое слово %s." % word)
                break

        return cleaned_data


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


    def clean(self):
        forbidden_words = os.getenv("FORBIDDEN_WORDS").split(",")
        cleaned_data = super().clean()

        cleaned_product = cleaned_data.get("name").split()
        for word in cleaned_product:
            if word.lower() in forbidden_words:
                self.add_error("name", "Поле с наименованием продукта содержит запрещённое слово %s." % word)
                break

        cleaned_description = cleaned_data.get("description").split()
        for word in cleaned_description:
            if word.lower() in forbidden_words:
                self.add_error("description", "Поле с описанием продукта содержит запрещённое слово %s." % word)
                break

        return cleaned_data
