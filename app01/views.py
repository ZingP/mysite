from django.shortcuts import HttpResponse, render

# from django.http import HttpResponse
from django.views import View

# def index(request):
#     ret = "<h1>{}</h1>".format("Hello, welcome to app01 index.")
#     return HttpResponse(ret)

def index(request):
    name = "liuyy"
    fruits = ["火龙果", "香蕉", "西瓜"]
    info = {
        "age": 26,
        "salary": 1000000,
    }
    return render(request, "index.html", {"name": name, "fruits": fruits, "user": info})

# function base views
def home(request):
    ret = None
    if request.method == "GET":
        ret = "Welcome to home."
    return HttpResponse(ret)

# class based view
class MyHome(View):

    def dispatch(self, request, *args, **kwargs):
        # 调用父类中的dispatch
        print('before')
        result = super(MyHome, self).dispatch(request, *args, **kwargs)
        print('after')
        return result

    def get(self, request):
        ret = "Welcome to my home"
        return HttpResponse(ret)

def simple(request):
    return render(request, "simple.html")

