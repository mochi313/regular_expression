import re
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"regex/index.html")

def confirm(request):
    if request.method == "POST":
        name = re.sub("\s","",request.POST.get("name"));
        age = request.POST.get("age");
        zip_code = request.POST.get("zip_code");
        tel = request.POST.get("tel");
        context = {
            "name":name,
            "age":age,
            "zip_code":zip_code,
            "tel":tel
        }
        if not re.match("^[0-9]+$",context["age"]):
            context["age"] = ""
        if not re.match("^\d{3}-?\d{4}$",context["zip_code"]):
            context["zip_code"] = ""
        if not re.match("^\d{3}-?\d{4}-?\d{4}$",context["tel"]):
            context["tel"] = ""
        if context["age"] == "" or context["zip_code"] == "" or context["tel"] == "":
            return render(request,"regex/index.html",{"context":context})
        return render(request,"regex/confirm.html",{"context":context})
    # print(context)
    return render(request,"regex/index.html")