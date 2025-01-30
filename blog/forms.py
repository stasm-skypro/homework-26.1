import os
from django import forms

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


    def clean(self):
        forbidden_words = os.getenv("FORBIDDEN_WORDS").split(",")
        cleaned_data = super().clean()
        cleaned_title = cleaned_data.get("title").split()
        for word in cleaned_title:
            if word.lower() in forbidden_words:
                self.add_error("title", "Поле с названием статьи содержит запрещённое слово %s." % word)
                break

        return cleaned_data
