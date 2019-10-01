from django.contrib import admin

from main.models.region import Region
from main.models.news import News
from main.models.media import Media
from main.models.registries import Registries
from main.models.file import File
from main.models.questions import Question
from main.models.articles import Articles
from main.models.documents import Document
from main.models.review import Review
from main.models.static_pages import StaticPage
from main.models.employees import Employee
from main.models.documens_parent import DocParent
from main.models.type_organ import TypeOrgan

admin.site.register(Region)
admin.site.register(Media)
admin.site.register(Registries)
admin.site.register(News)
admin.site.register(File)
admin.site.register(Question)
admin.site.register(Articles)
admin.site.register(Document)
admin.site.register(Review)
admin.site.register(StaticPage)
admin.site.register(Employee)
admin.site.register(DocParent)
admin.site.register(TypeOrgan)
