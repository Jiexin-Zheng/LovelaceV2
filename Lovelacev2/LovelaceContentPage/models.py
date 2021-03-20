from django.db import models

class LectureContent(models.Model):   # A Database model for the content on the page (Should probably be turned into a parent class with only Parent, index and content type)
    Parent = models.CharField(max_length=100,) # Parent field pointing to the lecture/course that the content is part of
    Index = models.PositiveIntegerField() # index of the content on the webpage. When the website is printed it goes through for loop and prints the content from index 0 -> 
    ContentType = models.CharField(max_length=100,) #Content type, Would be like image/text/ etc embedded content
    ContentText = models.CharField(max_length=1000,) #Content text, Should be only for the text content, probably should be in separate subclass that has this one as parent
    ContentHeader = models.CharField(max_length=100,) #Also only for text content. The header of the text content (Optional)
    ContentImageTitle = models.CharField(max_length=100,) #For Image content the title of the image (Should be subclass for image)
    ContentImageFile = models.ImageField(upload_to="static") #The file to be shown on the website
    def __str__(self): #A function that prints the queryset in shell
        string = str(self.Index) + self.ContentHeader + self.ContentText
        return (string)
    