import os
import json
from urllib.request import urlopen, Request  # noqa: 401
from urllib.error import HTTPError  # noqa: 401
import logging

logger = logging.getLogger(__name__)

DEFAULT_CITY = "London"
DEFAULT_COUNTRYCODE = "uk"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={app_id}"


class MyException(Exception):
    pass


def request(city, country_code):
    url = WEATHER_URL.format(
        city=city,
        country_code=country_code,
        app_id=os.environ.get("OPEN_WEATHER_API_KEY"),
    )
    logger.info(f"about to call API {url}")
    request = Request(url)

    try:
        response = urlopen(request)
    except HTTPError as e:
        raise MyException(e.reason)

    data = json.loads(response.read())
    return data


def main(city, country_code):
    data = {}
    try:
        data = request(city, country_code)
    except MyException as e:
        print(e)
    finally:
        return data


if __name__ == "__main__":
    main("New York", "us")
