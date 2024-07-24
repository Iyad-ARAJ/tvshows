from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['title']) < 2 :
            errors['title'] = 'the title must be at least 2 char'
        if len(postData['network']) < 3 :
            errors['network'] = 'network must be at least 3 char'
        if len(postData['description']) < 10 :
            errors['description'] = 'description must be at least 10 char'
        return errors



class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    objects = ShowManager()


def createshow(POST):
    show = Show.objects.create(title = POST['title'],network = POST['network'], release_date = POST['releasedate'], description = POST['description'])
    return show
# def createshow(title,network,release_date,description):
#     show = Show.objects.create(title = title,network = network,release_date=release_date,description=description)
#     return show


def getid(id):
    showid =Show.objects.get(id = id)
    return showid

def deleteshow(id):
    deleteshow = Show.objects.get(id =id )
    deleteshow.delete()

def allshows():
    return Show.objects.all()

def editshow(id):
    return Show.objects.get(id = id )