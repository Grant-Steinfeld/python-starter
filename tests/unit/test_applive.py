from src.services import app


def test_live_api_call():
    """ call the api live """
    actual = app.main("Berlin", "de")
    assert actual["name"] == "Berlin"
