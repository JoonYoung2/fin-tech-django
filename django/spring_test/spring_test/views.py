from rest_framework.response import Response
from rest_framework.decorators import api_view

from spring_test import bank_analysis

gbc = bank_analysis.init()

@api_view(['GET'])
def test(req):
    print("test연동")
    print(req.GET)
    print(req.GET['name'])
    return Response( {"key" : "success"} )

@api_view(['GET'])
def bank(req):
    print("bank 연동")
    print(req.GET)

    return Response({"key" : "success"})