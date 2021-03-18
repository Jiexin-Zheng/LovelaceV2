from django import forms

class TextForm(forms.Form):
    header_input = forms.CharField(label= " Enter Header:", max_length=100, empty_value="NoHeader", required=False)
    text_input = forms.CharField(label= " Enter paragraph:", max_length=1000, widget=forms.Textarea(attrs={"rows":30, "cols":40, "style":"resize:none;"}))
    index_input = forms.IntegerField(initial=100)
	
class DeleteForm(forms.Form):
    IndexToBeDeleted = forms.IntegerField(initial=100)
	
class ImageFileForm(forms.Form):
    imagetitle = forms.CharField(max_length=100)
    imagefile = forms.ImageField()
    image_index = forms.IntegerField(initial=100)