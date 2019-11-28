from django.contrib import admin

import main.admin.news
import main.admin.reestr
import main.admin.reestr_info
import main.admin.reestr_info_type
import main.admin.static_pages
import main.admin.media_file


from main.models.region import Region
from main.models.media import Media
from main.models.file import File
from main.models.questions import Question
from main.models.articles import Articles
from main.models.documents import Document
from main.models.review import Review
from main.models.employees import Employee
from main.models.documens_parent import DocParent
from main.models.documents_type import DocType
from main.models.type_organ import TypeOrgan
from main.models.sliders import Slider

admin.site.register(Region)
# admin.site.register(Media)
admin.site.register(File)
admin.site.register(Question)
# admin.site.register(Articles)
admin.site.register(Document)
# admin.site.register(Review)
admin.site.register(Employee)
admin.site.register(DocParent)
admin.site.register(TypeOrgan)
admin.site.register(Slider)
admin.site.register(DocType)
