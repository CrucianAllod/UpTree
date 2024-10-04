import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UpTree.settings')
django.setup()
from tree.models import Menu, MenuItem


def populate():
    main_menu = Menu.objects.create(name='Main Menu')

    about = MenuItem.objects.create(menu=main_menu, name='About', url='/about/')
    contact = MenuItem.objects.create(menu=main_menu, name='Contact', url='/contact/')
    team = MenuItem.objects.create(menu=main_menu, name='Team', parent=about, url='/about/team/')
    history = MenuItem.objects.create(menu=main_menu, name='History', parent=about, url='/about/history/')
    suda = MenuItem.objects.create(menu=main_menu, name='suda', parent=history, named_url='suda')

    print("Database populated with sample data.")

if __name__ == '__main__':
    populate()