from api import schema 
from ninja import NinjaAPI
from education.models import Topic
from api.auth import BasicAuth, AuthBearer


api_handlers = NinjaAPI(urls_namespace="api")


@api_handlers.post("/ping", tags=["Ping"])
def ping(request, data: schema.Ping_POST_IN): 
    data = data.dict()
    ping = data["ping"]
    return {"pong": ping}


@api_handlers.api_operation(["GET"], "/topic", tags=["Education"], response=schema.Topic_GET_OUT)
def topic(request, topic_id: int): 
    # lesson8
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Exception as e:
        return {"error": str(e)}
    return topic
    

# lesson9
@api_handlers.post("/ping_basic_auth", auth=BasicAuth(), tags=["PingBasicAuth"])
def ping_basic_auth(request, data: schema.Ping_POST_IN): 
    data = data.dict()
    ping = data["ping"]
    return {"pong": "ping_basic_auth"}   
 
# lesson9
@api_handlers.post("/ping_bearer_key", auth=AuthBearer(), tags=["PingBearerToken"])
def ping_bearer_token(request, data: schema.Ping_POST_IN): 
    data = data.dict()
    ping = data["ping"]
    return {"pong": "ping_bearer_key"}