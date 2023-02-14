from django.shortcuts import render,redirect
from .form import ImageForm
from .models import Image


def upload_view(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return redirect('upload_list')
    else:
        form=ImageForm()
    img=Image.objects.all()
    return render(request,"upload.html",{"img":img,"form":form})

def upload_list(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"upload_list.html",{"obj":obj})
    else:
        form=ImageForm()
    img=Image.objects.all()
    return render(request,"upload_list.html",{"img":img,"form":form})
