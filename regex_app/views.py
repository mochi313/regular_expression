import re
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"regex/index.html")

def confirm(request):
    if request.method == "POST":
        name = request.get("name");
        age = request.POST["age"];
        zip_code = request.POST["zip_code"];
        tel = request.POST["tel"];
    # name = re.sub(' ','',name)
    # if re.search('\D',age):
    #     age = ""
    # if re.search('^([0-9]|-)',zip_code):
    #     zip_code = ""
    # if re.search('^([0-9]|-)',tel):
    #     tel = ""
    context = {
        "name":name,
        "age":age,
        "zip_code":zip_code,
        "tel":tel
    }
    # print(context)
    return render(request,"regex/index.html",context)