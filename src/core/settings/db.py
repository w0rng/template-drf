from core.settings import env


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': env.str('POSTGRES_USER', 'postgres'),
        'HOST': env.str('POSTGRES_HOST', 'db'),
        'PASSWORD': env.str('POSTGRES_PASSWORD', 'postgres'),
        'PORT': env.str('POSTGRES_PORT', 5432),
    },
}
