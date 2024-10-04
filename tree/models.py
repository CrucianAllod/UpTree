from django.db import models
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=100, blank=True)
    named_url = models.CharField(max_length=100, blank=True)

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                pass
        if self.url:
            return self.url
        return '#'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'