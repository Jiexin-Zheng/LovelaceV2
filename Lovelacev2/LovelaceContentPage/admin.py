from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import LectureContent, TextContentModel, ImageContentModel

# Register your models here.
"""
class LectureContentInLine(admin.TabularInline):
	fieldsets = [
		(None, {'fields': ['Parent']}),
		#('Date information', {'fields': ['create_date']}),
	]
	model = LectureContent
	extra = 0
	show_change_link = True
	#readonly_fields = ('page_name','create_date',)
	list_display = ('Index', 'ContentType',)
"""

class TextContentModelInLine(admin.TabularInline):
	fieldsets = [
		(None, {'fields': ['ContentText']}),
		('HEADER', {'fields': ['ContentHeader']}),
	]
	model = TextContentModel
	extra = 0
	show_change_link = True
	#readonly_fields = ('page_name','create_date',)
	list_display = ('Index', 'ContentType',)
    
class LectureContentAdmin(admin.ModelAdmin):
    model = LectureContent
    inlines = [TextContentModelInLine]
    
    list_display = ('Index', 'Parent', 'ContentType', )


class TextContentModelAdmin(admin.ModelAdmin):
    model = TextContentModel
    #inlines 
    list_display = ('ContentHeader',)
    
admin.site.register(LectureContent, LectureContentAdmin)
admin.site.register(TextContentModel, TextContentModelAdmin)
