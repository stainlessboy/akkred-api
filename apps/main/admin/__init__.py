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
import main.admin.type_organ
import main.admin.inspection_control
import main.admin.inspection_control_category
import main.admin.slider
import main.admin.doc_parents
import main.admin.doc_type
from main.models import CategoryDocumentForm

from main.models.region import Region
from main.models.questions import Question
from main.models.employees import Employee

admin.site.register(Region)
admin.site.register(Question)
admin.site.register(Employee)
admin.site.register(CategoryDocumentForm)
