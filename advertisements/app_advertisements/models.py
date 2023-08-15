from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model


User = get_user_model()


class Advertisement(models.Model):

    user = models.ForeignKey(
        User,
        verbose_name='пользователь',
        on_delete=models.CASCADE,
    )

    image = models.ImageField(
        "изображение",
        upload_to='advertisements/'
    )

    #Заголовок
    #Небольшое текстовое поле
    title = models.CharField("Заголовок", max_length=128)

    # Описание
    description = models.TextField("Описание")

    # Цена
    # Число с фиксированной точностью
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

    # Дата создания
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения
    updated_at = models.DateTimeField(auto_now=True)

    # Уместен ли торг
    # Логическое значение
    auction = models.BooleanField("Торг", help_text="Отметьте, если хотите торговться")

    @admin.display(description="дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.strftime("%H:%M:%S")
            return format_html(
                "<span style='color:green; font-weight:bold; '> сегодня в {}</span>", 
                created_time
                )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='фото')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{}" style="max-height:80px; max-width:80px">',
                self.image.url
            )

    @admin.display(description="дата изменения")
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.strftime("%H:%M:%S")
            return format_html(
                "<span style='color:red; font-weight:bold; '> сегодня в {}</span>", 
                updated_time
                )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    def __str__(self):
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>"

    class Meta:
        db_table = 'advertisements'

    # Изображение

    # Адрес

    # Отзывы/рейтинг продавца

    # Контакты продавца

    # Похожие товары
