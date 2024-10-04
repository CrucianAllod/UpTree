from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import select_template
from django.views.generic import TemplateView

class GenericPageView(TemplateView):
    template_name = 'tree/base.html'

    def get_template_names(self):
        page_path = self.kwargs.get('page_path')
        segments = page_path.split('/') if page_path else []

        possible_templates = ['/'.join(segments[:i]) + '.html' for i in range(len(segments), 0, -1)]
        possible_templates.append(self.template_name)

        return select_template(possible_templates).template.name