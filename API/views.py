from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"]) # ["POST"] ["PUT"] ["DELETE"] ["__all__"]
def get_data(request):
	moscow = {"City": "Moscow", "Cond": "Sunny", "Temp": 25, "Wind": False}
	london = {"City": "London", "Cond": "Rain",  "Temp": 10, "Wind": True}
	
	city = moscow
	return Response(city)