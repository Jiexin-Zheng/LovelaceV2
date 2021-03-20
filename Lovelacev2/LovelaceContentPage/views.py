from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, loader, engines
from .forms import TextForm, DeleteForm, ImageFileForm
from .models import LectureContent

def index(request):
    List = []       #This list will contain all of the content to be rendered on the selected lecture
    List.clear() 
    indexnumber = 0   # index that will hold the max number of separate pieces of content on the website
    isBreak = False # No idea why this is here
    LectureContentObjects = LectureContent.objects.filter(Parent = "Lecture8")   # LectureContentObjects filters the lecture content from database that belongs to the selected course. In this case the "lecture8" is just an example, in real implementation it would be somehow inherited from the website that you can get to the lecture from.
    SortedLectureContentObjects = LectureContentObjects.order_by("Index")  #Sort the lecture specific content based on index so that it gets rendered in correct order.
    for i in SortedLectureContentObjects:    #a for loop that saves all the sorted lecture content into the list in order plus changes the indexes if there are "holes" in the order of them. for example if content with index 2 is deleted then the following indexes must be changed to make it work.
        if i.Index != indexnumber:   #this is the reordering part.
            i.Index = indexnumber
            i.save()
        List.append(i)
        indexnumber += 1
    template = loader.get_template("contentpage.html")
    if (request.method) == "POST":  #if a form is submitted it runs this part. Aka if image, or text is added or if deletion form is submitted to delete content.
        textform = TextForm(request.POST)  #gets the textform
        deleteform = DeleteForm(request.POST)
        imagefileform = ImageFileForm(request.POST, request.FILES)
        if textform.is_valid(): #if the user sends text content, then this will be true.
            text = textform.cleaned_data["text_input"]
            header = textform.cleaned_data["header_input"]
            enteredindex = textform.cleaned_data["index_input"] #the content  from the form must be apparently cleaned, that's why the .cleaned_data is here. enteredindex is the index of the content added.
            for j in SortedLectureContentObjects:  #again, when new content is added, the indexes that are as high or higher must be incremented so that the new content can be added in the middle.
                if j.Index >= enteredindex:
                    j.Index += 1
                    j.save()
            content = LectureContent(Parent = "Lecture8", Index = enteredindex, ContentType = "Text", ContentText = text, ContentHeader = header, ContentImageFile = "NoFile", ContentImageTitle = "NoTitle")
            content.save() #content is saved into database
            context = { 
                "List": List,
                "textform": textform,
                "indexnumber": indexnumber,
                "deleteform": deleteform,
				"imagefileform": imagefileform,
            }  #context has the variables used in this python file, they are passed into the template
            return HttpResponseRedirect("/LovelaceContentPage/")
        elif deleteform.is_valid():  #Deletion form is valid if the user fills a deletion form, aka presses the minus sign on the website.
            deletedindex = deleteform.cleaned_data["IndexToBeDeleted"]
            SortedLectureContentObjects.filter(Index=deletedindex).delete()
            for j in SortedLectureContentObjects:
                if j.Index > deletedindex:
                    j.Index -= 1
                    j.save()
            return HttpResponseRedirect("/LovelaceContentPage/")
        elif imagefileform.is_valid():  #basically the same a the text form, just different variables. 
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
            return HttpResponseRedirect("/LovelaceContentPage/")  #redirect back to the same page(reload page)
    else: #if no forms are sent, then they are just kept empty.
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
	