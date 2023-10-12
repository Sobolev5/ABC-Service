import pprint
from settings import BASE_DIR
from simple_print import sprint
from django.shortcuts import render, HttpResponse
from chat.forms import ChatMessageForm
from chat.models import ChatMessage
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def room_simple(request, room_name):
    # lesson5 lesson6 
    messages = []
    form = ChatMessageForm()
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            author = data["author"]
            message = data["message"]
            messages.append({"author": author, "message": message})

    return render(request, "chat/room.html", {"messages": messages, "form": form, "room_name":room_name})


def room_descriptor(request, room_id=None):
    # lesson5 lesson6 

    # print(RamDB.show_me_db())
    # print(ChatMessage.all())
    messages = ChatMessage.all()
    form = None
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            author = data["author"]
            message = data["message"]
            chat_message = ChatMessage(room_id=room_id, author=author, message=message)
            chat_message.save()

            # И так тоже можно:            
            
            # chat_message = ChatMessage()
            # chat_message.author = data["author"]
            # chat_message.message = data["message"]
            # chat_message.save()

    return render(request, "chat/room.html", {"messages": messages, "form": form, "room_id": room_id})


def http(request):
    
    # request (HTTP запрос от клиента)

    # заголовки
    sprint(request.headers) # дебажим при помощи sprint

    # query params (часть uri)    
    print(request.GET) # ?name=andrey&city=moscow

    # тело запроса
    print(request.body)

    response = HttpResponse(content="", content_type="text/html")
    response.write("\nHello world.") # Добавим что то в конец HTTP сообщения
    response.headers["Some-Error-Header"] = "Some strange errror"
    response.status_code = 500
    return response

    image_bytes = ""
    with open(f"{BASE_DIR}/static/scheduler.png", "rb") as f:
        image_bytes = f.read()    

    response = HttpResponse(content=image_bytes, content_type="image/png")
    response.status_code = 200   

    # Для сравнения https://www.django-rest-framework.org/tutorial/quickstart/
    return response
    

