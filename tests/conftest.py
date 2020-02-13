import json
import pytest
from urllib.error import HTTPError


class MockResponse(object):
    exception = False
    data = None

    def raise_exception(self):
        self.exception = True

    def read(self):
        data = self.data or {}
        return json.dumps(data)


@pytest.fixture
def mocked_urllib(monkeypatch):
    responses = {"weather": MockResponse()}

    def urlopen(request):
        # return the matching mock response
        # url = (
        #     request.get_full_url()
        # )
        # could parse weather out of url if need be if other api calls used say like mood etc
        key = "weather"
        response = responses[key]
        if response.exception:
            raise HTTPError("url", 500, "mock error for " + key, {}, None)
        return response

    from src.services import app

    with monkeypatch.context() as m:
        m.setattr(app, "urlopen", urlopen)
        yield responses
