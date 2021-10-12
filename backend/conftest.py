from datetime import timedelta

from hypothesis import settings

settings.register_profile("default", max_examples=5)
settings.load_profile("default")

settings.register_profile("ci", max_examples=100, deadline=timedelta(seconds=20))
