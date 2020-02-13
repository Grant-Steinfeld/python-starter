from src.services import app


def test_load_weather(mocked_urllib, capsys):
    mocked_urllib["weather"].data = getMockData()

    ret_ = app.request(
        42, 24
    )  # parameters here do not matter as this is a mocked call ...

    assert ret_["weather"][0]["main"] == "Clouds"
    assert ret_["weather"][0]["description"] == "few clouds"
    assert ret_["main"]["temp"] == 275.74
    assert ret_["main"]["pressure"] == 1013
    assert ret_["main"]["humidity"] == 74


def getMockData():
    return {
        "coord": {"lon": 13.41, "lat": 52.52},
        "weather": [
            {"id": 801, "main": "Clouds", "description": "few clouds", "icon": "02n"}
        ],
        "base": "stations",
        "main": {
            "temp": 275.74,
            "feels_like": 268.5,
            "temp_min": 274.26,
            "temp_max": 277.04,
            "pressure": 1013,
            "humidity": 74,
        },
        "visibility": 10000,
        "wind": {"speed": 7.2, "deg": 240},
        "clouds": {"all": 13},
        "dt": 1581558523,
        "sys": {
            "type": 1,
            "id": 1275,
            "country": "DE",
            "sunrise": 1581575284,
            "sunset": 1581610398,
        },
        "timezone": 3600,
        "id": 2950159,
        "name": "Berlin",
        "cod": 200,
    }
