from model_bakery.recipe import Recipe

from .enums import UserStatusChoice

active_user = Recipe(
    "accounts.UserAccount",
    status=UserStatusChoice.USE,
    is_staff=False,
    _fill_optional=True,
)
