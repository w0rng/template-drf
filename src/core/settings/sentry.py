from core.settings import env
from sentry_sdk.integrations.django import DjangoIntegration


if env.bool('USE_SENTRY', False):
    import sentry_sdk

    sentry_sdk.init(
        dsn=env.str('SENTRY_DSN'),
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )
