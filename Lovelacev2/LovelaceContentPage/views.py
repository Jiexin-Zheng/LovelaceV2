from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, loader, engines
from .forms import TextForm, DeleteForm, ImageFileForm, EmbeddedFileForm
from .models import LectureContent, ImageContentModel, TextContentModel, FileContentModel
import LovelaceContentPage.markupparser as markupparser
import LovelaceContentPage.blockparser as blockparser
from django.http import JsonResponse
import os

def index(request):
<<<<<<< HEAD
    TemporaryCurrentLecture = "Lecture14"
    List = []       #This list will contain all of the content to be rendered on the selected lecture
    List.clear() 
    ListOfTemplates = [x for x in os.listdir("LovelaceContentPage/templates") if x.endswith(".html") and x != "contentpage.html"]
    Choicelist = []
    for choice in ListOfTemplates:
        Choicelist.append((choice, choice))
    indexnumber = 0   # index that will hold the max number of separate pieces of content on the website
    isBreak = False # No idea why this is here
    LectureContentObjects = LectureContent.objects.filter(Parent = TemporaryCurrentLecture)  # LectureContentObjects filters the lecture content from database that belongs to the selected course. In this case the "lecture8" is just an example, in real implementation it would be somehow inherited from the website that you can get to the lecture from.
    SortedLectureContentObjects = LectureContentObjects.order_by("Index")  #Sort the lecture specific content based on index so that it gets rendered in correct order.
    for i in SortedLectureContentObjects:    #a for loop that saves all the sorted lecture content into the list in order plus changes the indexes if there are "holes" in the order of them. for example if content with index 2 is deleted then the following indexes must be changed to make it work.
        if i.Index != indexnumber:   #this is the reordering part.
=======
    List = [] #testikommentti
    List.clear()
    indexnumber = 0
    isBreak = False
    LectureContentObjects = LectureContent.objects.filter(Parent = "Lecture8")
    SortedLectureContentObjects = LectureContentObjects.order_by("Index")
    for i in SortedLectureContentObjects:
        if i.Index != indexnumber:
>>>>>>> 51fd0f14d99b4490812a4192fc029b7101953c62
            i.Index = indexnumber
            i.save()
        List.append(i)
        indexnumber += 1
    template = loader.get_template("contentpage.html")
    if (request.method) == "POST":  #if a form is submitted it runs this part. Aka if image, or text is added or if deletion form is submitted to delete content.
        textform = TextForm(request.POST)  #gets the textform
        deleteform = DeleteForm(request.POST)
        imagefileform = ImageFileForm(request.POST, request.FILES)
        fileform = EmbeddedFileForm(request.POST, Choicelist = Choicelist)
        print("jiijji")
        if textform.is_valid(): #if the user sends text content, then this will be true.
            text = textform.cleaned_data["text_input"]
            textparsed = "".join(markupparser.MarkupParser.parse(text))
            header = textform.cleaned_data["header_input"]
            editmode = textform.cleaned_data["EditMode"]
            enteredindex = textform.cleaned_data["index_input"] #the content  from the form must be apparently cleaned, that's why the .cleaned_data is here. enteredindex is the index of the content added.
            if editmode == "False":
                for j in SortedLectureContentObjects:  #again, when new content is added, the indexes that are as high or higher must be incremented so that the new content can be added in the middle.
                    if j.Index >= enteredindex:
                        j.Index += 1
                        j.save()
                content = TextContentModel(Parent = TemporaryCurrentLecture, Index = enteredindex, ContentType = "Text", ContentText = textparsed, ContentTextNotParsed = text, ContentHeader = header)
                content.save() #content is saved into database
            if editmode == "True":
                content = SortedLectureContentObjects.filter(Parent = TemporaryCurrentLecture, Index = enteredindex).delete()
                newcontent = TextContentModel(Parent = TemporaryCurrentLecture, Index = enteredindex, ContentType = "Text", ContentText = textparsed, ContentTextNotParsed = text, ContentHeader = header)
                newcontent.save() #content is saved into database
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
            imagecaption = imagefileform.cleaned_data["imagecaption"]
            enteredindex = imagefileform.cleaned_data["image_index"]
            editmodeimage = imagefileform.cleaned_data["EditModeImage"]
            if editmodeimage == "False":
                for j in SortedLectureContentObjects:
                    if j.Index >= enteredindex:
                        j.Index += 1
                        j.save()
                content = ImageContentModel(Parent = TemporaryCurrentLecture, Index = enteredindex, ContentType = "Image", ContentImageTitle = imagefiletitle, ContentImageFile = imagefile, ContentImageCaption = imagecaption)
                content.save()
            if editmodeimage == "True":
                temporaryobj = SortedLectureContentObjects.get(Parent = TemporaryCurrentLecture, Index = enteredindex)
                tempimagefile = temporaryobj.imagecontentmodel.ContentImageFile
                SortedLectureContentObjects.filter(Parent = TemporaryCurrentLecture, Index = enteredindex).delete()
                newcontent = ImageContentModel(Parent = TemporaryCurrentLecture, Index = enteredindex, ContentType = "Image", ContentImageTitle = imagefiletitle, ContentImageFile = tempimagefile, ContentImageCaption = imagecaption)
                newcontent.save() #content is saved into database
            return HttpResponseRedirect("/LovelaceContentPage/")  #redirect back to the same page(reload page)
        elif fileform.is_valid():
            filetitle = fileform.cleaned_data["filetitle"]       
            file = fileform.cleaned_data["file"] 
            enteredindex = fileform.cleaned_data["file_index"]
            editmodefile = fileform.cleaned_data["EditModeFile"]
            if editmodefile == "False":
                for j in SortedLectureContentObjects:
                    if j.Index >= enteredindex:
                        j.Index += 1
                        j.save()
                content = FileContentModel(Parent = TemporaryCurrentLecture, Index = enteredindex, ContentType = "File", ContentFileTitle = filetitle, ContentFile = file)
                content.save()
            if editmodefile == "True":
                temporaryobj = SortedLectureContentObjects.get(Parent = TemporaryCurrentLecture, Index = enteredindex)
                tempfile = temporaryobj.imagecontentmodel.ContentFile
                SortedLectureContentObjects.filter(Parent = TemporaryCurrentLecture, Index = enteredindex).delete()
                newcontent = FileContentModel(Parent = TemporaryCurrentLecture, Index = enteredindex, ContentType = "File", ContentFileTitle = filetitle, ContentFile = tempfile)
                newcontent.save() #content is saved into database
            return HttpResponseRedirect("/LovelaceContentPage/")
    else: #if no forms are sent, then they are just kept empty.
        textform = TextForm()
        deleteform = DeleteForm()
        imagefileform = ImageFileForm()
        fileform = EmbeddedFileForm(Choicelist = Choicelist)
    context = {
        "List": List,
        "textform": textform,
        "indexnumber": indexnumber,
		"deleteform": deleteform,
        "imagefileform": imagefileform,
        "fileform": fileform
    }
    return HttpResponse(template.render(context, request))


def example1view(request):
    template = loader.get_template("example1.html")
    test = "Test"
    context = {
        "test": test,
    }
    return HttpResponse(template.render(context, request))

def example2view(request):
    template = loader.get_template("example2.html")
    test = "Test2"
    context = {
        "test": test,
    }
    return HttpResponse(template.render(context, request))
