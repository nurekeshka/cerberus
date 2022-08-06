from django.views.generic import TemplateView
from .models import Password


class PasswordsView(TemplateView):
    template_name = 'passwords/passwords.html'

    def get_context_data(self, **kwargs) -> dict:
        passwords = Password.objects.all()

        context = {
            'passwords': passwords
        }

        return context
