from django.db import models


class ItemModel(models.Model):
    """
    Модель элементов списка дел
    """
    name = models.CharField(max_length=128, verbose_name='Название элемента')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, blank=True)
    listmodules = models.ForeignKey('main.ListModel', on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    expr_date = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'Элементы'
        verbose_name_plural = 'Элементы'
        unique_together = ('name', 'listmodules_id')
