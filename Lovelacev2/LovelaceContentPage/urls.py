from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

createdurls = []

def createurlpatterns(List):
	for i in List:
		if i not in createdurls:
			createdurls.append(i)
			urlpatterns.append(path(i, views.example1view, name=i))

def createexerciseurlpatterns(List):
	print("\n konnaaaa", List)
	for i in List:
		print(createdurls)
		if i[0] not in createdurls:
			createdurls.append(i[0])
			urlpatterns.append(path(i[0], views.Exercise, {'Context': {
				"indexofquestion": str(i[0]),
				"ExerciseQuestion": i[1],
				"ExerciseType": i[2],
				}}, name=str(i[0])))

def urlreset(urlpatterns):
	createdurls.clear()
	urlpatterns.clear()
	urlpatterns.append(path('', views.index, name='index'))