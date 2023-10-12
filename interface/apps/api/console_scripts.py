
import pprint
import requests
import ujson
from simple_print import sprint
from settings import HOST


class ApiTest:
    
    bearer_token = "Bearer yp2"

    @classmethod
    def get_auth_header(cls):
        return {"Authorization": cls.bearer_token}

    def ping(self):
        url = f"http://{HOST}/api/ping"
        sprint(f"ApiTest.ping url={url}", c="blue", b="on_white", p=1)
        data = {}
        data["ping"] = "pong"
        data = ujson.dumps(data).encode()

        response = {}
        try:
            response = requests.request("POST", url, data=data, headers={})
            response = response.text
        except Exception as e:
            sprint(e, c="red", p=1)
        
        if response:
            try:
                response = ujson.loads(response)
            except Exception as e:
                sprint(e, c="red", p=1) 

        return response




def test_ping():
    api_test = ApiTest()



