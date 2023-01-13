from django.http import HttpResponse

from .robot.robot import Robot

robot = Robot()

def index(request):
    for key in ["phone", "text"]:
        if key not in request.GET.keys():
            raise Exception(f"{key} is missing in request")

    params = {
        "phone" : request.GET["phone"],
        "text": request.GET["text"]
    }
    robot.send_message(params)
    phone, text = params.values()
    return HttpResponse(f"I have delivered the message to {phone}. Here it is: \n{text}")
