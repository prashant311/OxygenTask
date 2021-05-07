import operator

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import OxygenModel
from .serializer import OxygenSerializer


@csrf_exempt
def oxy_list(request):

    if request.method == "GET":
        query_set = OxygenModel.objects.order_by('-verifiedStatus', 'timeStamp')
        serializer = OxygenSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def oxy_create(request):

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = OxygenSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

        return JsonResponse(serializer.errors, status=400)


