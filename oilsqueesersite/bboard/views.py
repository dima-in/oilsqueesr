from django.shortcuts import render
from .models import Bb

"""
views - контроллеры
"""

def index(request):
    """
    loader.get_template('bboard/index.html'):
    загружает шаблон из папки templates

    Bb.objects.order_by('-published'):
    возвращает экземпляр объявления, сортированный
    по дате начиная с последней

    context = {'bbs': bbs}: контекст шаблона в формате
    словаря, ключи одноименные с переменными

    "длинная" версия index(request)
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}

    :param request:
    :return:
    """
    bbs = Bb.objects.all()

    return render(request, 'bboard/index.html', {'bbs': bbs})
