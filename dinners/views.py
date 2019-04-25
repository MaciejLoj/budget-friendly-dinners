from django.views.generic.base import TemplateView


class HomepageView(TemplateView):

    template_name = 'home-2.html'


class ContactView(TemplateView):

    template_name = 'contact.html'

