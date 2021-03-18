from django.db import models

class LectureContent(models.Model):
    Parent = models.CharField(max_length=100,)
    Index = models.PositiveIntegerField()
    ContentType = models.CharField(max_length=100,)
    ContentText = models.CharField(max_length=1000,)
    ContentHeader = models.CharField(max_length=100,)
    ContentImageTitle = models.CharField(max_length=100,)
    ContentImageFile = models.ImageField(upload_to="static")
    def __str__(self):
        string = str(self.Index) + self.ContentHeader + self.ContentText
        return (string)