import os.path


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

ALLOWED_HOSTS = ['*']

TEST_RUNNER = 'helpers.disable_test_command_runner.DisableTestCommandRunner'
