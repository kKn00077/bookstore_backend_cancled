from model_bakery.recipe import Recipe

from .enums import UserStatusChoice
from django.utils import timezone
from datetime import timedelta

active_user = Recipe(
    "accounts.UserAccount",
    status=UserStatusChoice.USE,
    is_staff=False,
    _fill_optional=True,
)

certification = Recipe(
    "accounts.Certification",
    is_verified=False,
    code="011001",
    limit_time = timezone.now() + timedelta(minutes=3),
    _fill_optional=True,
)
