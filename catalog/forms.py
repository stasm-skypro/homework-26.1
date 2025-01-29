"""
Формы для ввода данных.
"""

from django import forms
from django.forms import ClearableFileInput

from catalog.models import Contact, Product


# class ContactForm(forms.ModelForm):
#     """Класс для определения формы ввода для шаблона contacts."""
#
#     class Meta:
#         model = Contact
#         fields = ["first_name", "phone", "message"]
#         widgets = {
#             "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваше имя"}),
#             "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Контактный телефон"}),
#             "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Сообщение"}),
#         }

#
# class ProductForm(forms.ModelForm):
#     """Класс для определения формы создания и редактирования товара."""
#
#     class Meta:
#         model = Product
#         fields = ["product", "description", "image", "category", "price", "created_at", "changed_at"]
#         widgets = {
#             "product": forms.TextInput(attrs={"class": "form-control", "placeholder": "Наименование продукта"}),
#             "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Описание"}),
#             "image": ClearableFileInput(attrs={"class": "form-control"}),
#             "category": forms.TextInput(attrs={"class": "form-control", "placeholder": "Категория"}),
#             "price": forms.TextInput(attrs={"class": "form-control", "placeholder": "Цена"}),
#             "created_at": forms.TextInput(attrs={"class": "form-control", "placeholder": "Дата производства"}),
#             "changed_at": forms.TextInput(attrs={"class": "form-control", "placeholder": "Дата упаковки"}),
#         }
