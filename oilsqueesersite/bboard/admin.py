"""
регистрация приложения в списке административного сайта
"""

from django.contrib import admin

from .models import Bb
"""
класс редактор 
"""
class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published')
    """
    list_display: последовательность имен полей, выводятся
     в списке записей
    """
    list_display_links = ('title', 'content')
    """
    имена полей, преобразуются в гиперссылки,
    ведущие на станицу правки
    """
    search_fields = ('title', 'content', )
    """
    последовательность имен полей, по которым должна 
    выполняться фильтрация
    """

"""
register(): метод экземпляра класса AdminSite 
"""

admin.site.register(Bb)