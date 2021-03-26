from django import forms

class TextForm(forms.Form): #A form to enter text content on the website
    header_input = forms.CharField(label= " Enter Header:", max_length=100, required=False)
    text_input = forms.CharField(label= " Enter paragraph:", max_length=1000, widget=forms.Textarea(attrs={"rows":30, "cols":40, "style":"resize:none;"}))
    index_input = forms.IntegerField(initial=100)
	
class DeleteForm(forms.Form): #A form to delete a piece of content from the website
    IndexToBeDeleted = forms.IntegerField(initial=100)
	
class ImageFileForm(forms.Form): # A form to enter an image to the website
    imagetitle = forms.CharField(max_length=100, required=False)
    imagefile = forms.ImageField()
    imagecaption = forms.CharField(max_length=100, required=False)
    image_index = forms.IntegerField(initial=100)