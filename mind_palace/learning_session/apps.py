from django.apps import AppConfig


class SessionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # TODO: Remove old learning app and replace with the new one
    name = 'mind_palace.learning_session'
