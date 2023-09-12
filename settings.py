from pydantic import BaseModel
from cat.mad_hatter.decorators import hook


class MySettings(BaseModel):
    number_of_results: int = 10


@hook
def plugin_settings_schema():
    return MySettings.schema()
