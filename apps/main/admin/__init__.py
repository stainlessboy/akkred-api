from django.contrib import admin

import main.admin.news
import main.admin.reestr
import main.admin.reestr_info
import main.admin.reestr_info_type
import main.admin.static_pages
import main.admin.media_file
import main.admin.sat_ques
import main.admin.reestr_conf
import main.admin.document

from main.models.region import Region
from main.models.file import File
from main.models.questions import Question
from main.models.employees import Employee
from main.models.documens_parent import DocParent
from main.models.documents_type import DocType
from main.models.type_organ import TypeOrgan
from main.models.sliders import Slider

admin.site.register(Region)
admin.site.register(File)
admin.site.register(Question)
admin.site.register(Employee)
admin.site.register(DocParent)
admin.site.register(TypeOrgan)
admin.site.register(Slider)
admin.site.register(DocType)
