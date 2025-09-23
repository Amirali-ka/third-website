from django.shortcuts import render,HttpResponseRedirect
from mywebsite.forms import newsletterform,contactform
from django.contrib import messages
def index_view(request):
    return render(request,'index.html')
def about_view(request):
    return render(request,'about.html')
def contact_view(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            contact=form.save(commit=False)
            contact.save()
            messages.add_message(request,messages.SUCCESS,'your submit is successful')
        else:
           messages.add_message(request,messages.ERROR,'your submit is not successful') 
    else:
        form=contactform()
    return render(request,'contact.html',{'form':form})
def newsletter_view(request):
    if request.method=='POST':
        form=newsletterform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your submit is successful') 
            return HttpResponseRedirect('/') 
        else :
            messages.add_message(request,messages.ERROR,'your submit is not successful')
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')   
def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)