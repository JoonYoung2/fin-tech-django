from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    print("test 연결 성공!!!!")
    return HttpResponse("연결 성공!!!")

def ajax(request):
    return render(request, "ajax.html")

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['get', 'post', 'put', 'delete'])
def result(request):
    print(request.method, " : result 연동 성공????")
    if request.method == 'GET':
        data = {"execute" : "데이터 요청시 사용"}
    elif request.method == 'POST':
        data = {"execute" : "데이터 추가시 사용"}
    elif request.method == 'PUT':
        data = {"execute" : "데이터 수정시 사용"}
    elif request.method == 'DELETE':
        data = {"execute" : "데이터 삭제시 사용"}
    
    return Response(data)