from django.shortcuts import render
from django.http import JsonResponse
import logging
# Create your views here.

def home(request):
    output = "Hello, World!"
    logging.info(output)  # 记录输出
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return  render(request,'signup.html')
def check(request):
    return render(request,'zz.html')
    # if request.method == 'POST' and request.is_ajax():
    #     # 获取前端发送的数据
    #     key1 = request.POST.get('key1')
    #
    #
    #     # 构建响应数据
    #     response_data = {
    #         '123': key1,
    #         'message': 'Request processed successfully',
    #         'result': 'Some result data'
    #     }
    #
    #     # 返回JSON响应
    #     return JsonResponse(response_data)
    #
    #     # 处理其他请求方法或非AJAX请求
    # return JsonResponse({'error': 'Invalid request'})