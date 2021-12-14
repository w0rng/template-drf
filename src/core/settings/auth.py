AUTH_USER_MODEL = 'user.User'
LOGIN_URL = '/admin/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MIN_PASSWORD_LENGTH = 8

# Backends
AUTHENTICATION_BACKENDS = (
    'apps.user.authenticate_backend.MultipleFieldsAuthBackend',
)
