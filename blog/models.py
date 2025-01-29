from django.db import models

class Blog(models.Model):
    """
    Модель таблицы blog.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    preview = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to="blog/")
    created_at = models.DateField(auto_now_add=True)
    publicated = models.BooleanField(default=False)
    views_counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"{self.__class__} {self.title}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ("-created_at",)
