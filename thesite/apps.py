from django.apps import AppConfig


class ThesiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'thesite'

    def ready(self):
        import thesite.signals
