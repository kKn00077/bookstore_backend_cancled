from model_bakery.recipe import Recipe

meeting = Recipe(
    "meetings.Meeting",
    status="CAN_APPLY",
    _fill_optional=True,
)
