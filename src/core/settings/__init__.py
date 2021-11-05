from split_settings.tools import include
from core.settings.environ import env


SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)


include(
    'boilerplate.py',
    'db.py',
    'installed_apps.py',
    'locale.py',
    'middleware.py',
    'constance.py',
    'drf.py',
    'sentry.py',
    'static.py',
    'media.py',
    'templates.py',
)
