from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import os
from django.core.files.storage import FileSystemStorage

class FileOverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length = 100):
        if self.exists(name):
            os.remove(os.path.join(name))
        return name


class LectureContent(models.Model):   # A Database model for the content on the page (Should probably be turned into a parent class with only Parent, index and content type)
    Parent = models.CharField(max_length=100,) # Parent field pointing to the lecture/course that the content is part of
    Index = models.PositiveIntegerField() # index of the content on the webpage. When the website is rendered it goes through a for loop and renders the content from index 0 forwards in order.
    ContentType = models.CharField(max_length=100,) #Content type, Would be like image/text/ etc embedded content

class TextContentModel(LectureContent):
    ContentText = models.CharField(max_length=1000,)
    ContentTextNotParsed = models.CharField(max_length=1000,)
    ContentHeader = models.CharField(max_length=100,)
	
class ImageContentModel(LectureContent):
    ContentImageTitle = models.CharField(max_length=100,)
    ContentImageFile = models.ImageField(upload_to="static", storage= FileOverwriteStorage(), max_length= 100,)
    ContentImageCaption = models.CharField(max_length=100,)
    def __str__(self): #A function that prints the queryset in shell
        string = self.ContentImageTitle + self.ContentImageFile.url
        return(string)

class FileContentModel(LectureContent):
    ContentFileTitle = models.CharField(max_length=100,)
    ContentFile = models.CharField(max_length=100,)

class EmbeddedExerciseModel(LectureContent):
    ContentExerciseText = models.CharField(max_length=1000,)
    ContentExerciseTextNotParsed = models.CharField(max_length=1000,)
    ContentExerciseType = models.CharField(max_length=100,)
