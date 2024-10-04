from django import template
from django.shortcuts import get_object_or_404
from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('tree/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu = get_object_or_404(Menu, name=menu_name)
    menu_items = menu.items.select_related('parent').all()

    current_url = request.path
    active_item = None
    for item in menu_items:
        item_url = item.get_url()
        if item_url == current_url:
            active_item = item
            break

    menu_tree = build_tree(menu_items, active_item)

    return {
        'menu_tree': menu_tree,
        'active_item': active_item,
    }


def build_tree(items, active_item=None, parent=None):
    tree = []
    for item in items:
        if item.parent == parent:
            is_active = item == active_item
            children = build_tree(items, active_item, item)

            should_expand = is_active or any(child[2] for child in children) or (
                        active_item and item == active_item.parent)
            if active_item:
                parent_item = active_item.parent
                while parent_item:
                    if parent_item == item:
                        should_expand = True
                        break
                    parent_item = parent_item.parent
            tree.append((item, children if should_expand else [], is_active))
    return tree



