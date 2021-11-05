import environ


env = environ.Env()

environ.Env.read_env('.env')

__all__ = [
    env,
]
