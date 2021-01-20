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
    expr_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'@id={self.id}@name={self.name}@list={self.list_model.name}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        items = ItemModel.objects.filter(listmodules=self.listmodules)
        if all([item.is_done for item in items]):
            self.listmodules.is_done = True
            self.listmodules.save()
        else:
            self.listmodules.is_done = False
            self.listmodules.save()

    class Meta:
        verbose_name = 'Элементы'
        verbose_name_plural = 'Элементы'
        unique_together = ('name', 'listmodules')
