from django.apps import AppConfig


class Board1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board1'

    def ready(self):
        import board1.signals
