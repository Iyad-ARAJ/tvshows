from django.shortcuts import render,redirect
from . import models
from django.contrib import messages


def add_new_show(request):   
    return render(request,'addshow.html')

def create_show(request):
    if request.method == 'POST':
        errors = models.Show.objects.basic_validator(request.POST) 
        if len(errors) > 0 :
            for error in errors.values():
                messages.error(request,error)       #to not delete the inputs after an invalid input
            return render(request,'addshow.html',{'data':request.POST})
        else:
            show =models.createshow(request.POST)
        return redirect(f"/shows/{show.id}")
    
def show_details(request,id):
    context = { 
        'show' : models.getid(id=id)
    }
    return render(request,'show-details.html',context)

def delete_show(request,id):
    models.deleteshow(id)
    return redirect('/shows')

def all_shows(request):
    context= {
        'shows' : models.allshows(),
    
    }
    return render(request,'all-shows.html',context)

def edit_show(request,id):
    show = models.editshow(id) 
    show.release_date = show.release_date.strftime('%Y-%m-%d')
    context = {
        'show' : show
    }
    return render(request,'edit.html',context)
def update_show(request,id):
    if request.method == 'POST':
        show = models.editshow(id)
        errors = models.Show.objects.basic_validator(request.POST)  # TO CHECK VALIDATION DURING UPDATE
        if len(errors) > 0 :
            for error in errors.values():
                messages.error(request,error)
            return redirect(f'/shows/{show.id}/edit')
        else:
            post = request.POST
            show.title = post ['title']
            show.network = post['network']
            show.release_date = post['release_date']
            show.description = post['description']
            show.save()
            return redirect(f'/shows/{show.id}')


    