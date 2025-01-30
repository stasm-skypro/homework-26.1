import os
from django import forms
from django.core.exceptions import ValidationError

from blog.models import Blog
from dotenv import load_dotenv


load_dotenv()


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        labels = {
            "title": "Название статьи",
            "content": "Содержимое",
            "preview": "Миниатюра",
            "created_at": "Дата создания",
            "publicated": "Признак публикации",
            "views_counter": "Количество просмотров",
        }


    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                "class": "form-control",
                "placeholder": self.fields[field].label,
                "style": "font-size: 0.9em; width: 100%",
            })


    def clean_image_format(self):
        """
        Проверяет, что загружаемое изображение продукта в формате .jpg или .png.
        """
        image = self.cleaned_data.get("image")
        if image:
            valid_extensions = [".jpg", ".jpeg", ".png"]
            ext = os.path.splitext(image.name)[1].lower()
            if ext not in valid_extensions:
                raise ValidationError("Допустимые форматы изображений: .jpg, .jpeg, .png.")

        return image

    def clean_image_size(self):
        """
        Проверяет, что загружаемый файл изображения не превышает 5 МБ.
        """
        image = self.cleaned_data.get("image")
        max_size = 5 * 1024 * 1024  # 5 MБ

        if image and image.size > max_size:
            raise ValidationError("Размер изображения не должен превышать 5 МБ.")

        return image


    def clean(self):
        forbidden_words = os.getenv("FORBIDDEN_WORDS").split(",")
        cleaned_data = super().clean()
        cleaned_title = cleaned_data.get("title").split()
        for word in cleaned_title:
            if word.lower() in forbidden_words:
                self.add_error("title", "Поле с названием статьи содержит запрещённое слово %s." % word)
                break

        cleaned_content = cleaned_data.get("content")
        for word in forbidden_words:
            if word in cleaned_content:
                self.add_error("content", "Статья содержит запрещённое слово %s." % word)
                break

        return cleaned_data
