from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, loader, engines
from .forms import TextForm, DeleteForm, ImageFileForm
from .models import LectureContent

def index(request):
    List = [] #testikommentti
    List.clear()
    indexnumber = 0
    isBreak = False
    LectureContentObjects = LectureContent.objects.filter(Parent = "Lecture8")
    SortedLectureContentObjects = LectureContentObjects.order_by("Index")
    for i in SortedLectureContentObjects:
        if i.Index != indexnumber:
            i.Index = indexnumber
            i.save()
        List.append(i)
        indexnumber += 1
    template = loader.get_template("contentpage.html")
    if (request.method) == "POST": 
        textform = TextForm(request.POST)
        deleteform = DeleteForm(request.POST)
        imagefileform = ImageFileForm(request.POST, request.FILES)
        if textform.is_valid():
            text = textform.cleaned_data["text_input"]
            header = textform.cleaned_data["header_input"]
            enteredindex = textform.cleaned_data["index_input"]
            for j in SortedLectureContentObjects:
                if j.Index >= enteredindex:
                    j.Index += 1
                    j.save()
            content = LectureContent(Parent = "Lecture8", Index = enteredindex, ContentType = "Text", ContentText = text, ContentHeader = header, ContentImageFile = "NoFile", ContentImageTitle = "NoTitle")
            content.save()
            context = {
                "List": List,
                "textform": textform,
                "indexnumber": indexnumber,
                "deleteform": deleteform,
				"imagefileform": imagefileform,
            }
            return HttpResponseRedirect("/LovelaceContentPage/")
        elif deleteform.is_valid():
            deletedindex = deleteform.cleaned_data["IndexToBeDeleted"]
            SortedLectureContentObjects.filter(Index=deletedindex).delete()
            for j in SortedLectureContentObjects:
                if j.Index > deletedindex:
                    j.Index -= 1
                    j.save()
            return HttpResponseRedirect("/LovelaceContentPage/")
        elif imagefileform.is_valid():
            imagefiletitle = imagefileform.cleaned_data["imagetitle"]		
            imagefile = imagefileform.cleaned_data["imagefile"]	
            enteredindex = imagefileform.cleaned_data["image_index"]
            for j in SortedLectureContentObjects:
                if j.Index >= enteredindex:
                    j.Index += 1
                    j.save()
            content = LectureContent(Parent = "Lecture8", Index = enteredindex, ContentType = "Image", ContentText = "NoText", ContentHeader = "NoHeader", ContentImageFile = imagefile, ContentImageTitle = imagefiletitle)
            content.save()
            print(content)
            return HttpResponseRedirect("/LovelaceContentPage/")
    else:
        textform = TextForm()
        deleteform = DeleteForm()
        imagefileform = ImageFileForm()
    context = {
        "List": List,
        "textform": textform,
        "indexnumber": indexnumber,
		"deleteform": deleteform,
		"imagefileform": imagefileform,
    }
    return HttpResponse(template.render(context, request))
	