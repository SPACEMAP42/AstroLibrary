from datetime import datetime
from zoneinfo import ZoneInfo


def convert_datetime(str_datetime):
    return datetime.strptime(str_datetime, "%Y-%m-%dT%H:%M:%S.%fZ").replace(
        tzinfo=ZoneInfo("UTC")
    )
