from django.db import models

"""
Модель является подклассом класса Model django.db.models
"""
class Bb(models.Model):

    """
    Полям модели присваиваются экземпляры классов,
    параметры указываются в конструкторах в виде значений именованных параметров
    Отдельный экземпляр класса представляет отдельную запись в БД,
    позволяет получать и вносить в них значения

    """
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True,
                               verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name='Опубликовано')


    class Meta:
        """
        verbose_name_plural:
        название модели во множественном числе
        verbose_name:
        название модели в единственном числе
        ordering: последовательность полей для сортировки
        по умолчанию
        """
        verbose_name_plural = 'Объявления'
        verbose_name = 'объявление'
        ordering = ['-published']