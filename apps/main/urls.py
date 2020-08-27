from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views.authorized_reestr import AuthorizedReestrViewSet
from main.views.calculcation import Calculation
from main.views.confirm_reestr import ConfirmReestrViewSet
from main.views.doc_parents import DocParentViewSet, DocTypeViewSet, \
    CategoryDocumentFormViewSet
from main.views.file import FileViewSet
from main.views.inspection_control import ICCategoryViewSet, \
    InspectionControlViewSet
from main.views.menu import LanguageViewSet
from main.views.reestr_for_tamojnya import RegistriesForTamojnyaViewSet
from main.views.reestr_info import ReestrInfoUserViewSet
from main.views.sat_uestionnaire import SatisfactionQuestionnaireViewSet
from main.views.static_pages import StaticPagesViewSet
from main.views.user import UserViewSet
from main.views.news import NewsViewSet
from main.views.region import RegionViewSet
from main.views.sliders import SliderViewSet
from main.views.documents import DocumentViewSet
from main.views.employees import EmployeeViewSet
from main.views.registries import RegistriesViewSet, ReestrStatusViewSet
from main.views.type_organ import TypeOrganViewSet

router = DefaultRouter()
router.register('', UserViewSet, 'user')
router.register('file', FileViewSet, 'file')
router.register('doc-parent', DocParentViewSet, 'doc-parent')
router.register('doc-type', DocTypeViewSet, 'doc-type')
router.register('news', NewsViewSet, 'news')
router.register('static-pages', StaticPagesViewSet, 'static-pages')
router.register('region', RegionViewSet, 'region')
router.register('sliders', SliderViewSet, 'sliders')
router.register('documents', DocumentViewSet, 'documents')
router.register('employees', EmployeeViewSet, 'employees')
router.register('type-organ', TypeOrganViewSet, 'type-organ')
router.register('registries', RegistriesViewSet, 'registries')
router.register('reestr-info', ReestrInfoUserViewSet, 'reestr-info')
router.register('sat-quest', SatisfactionQuestionnaireViewSet, 'sat-quest')
router.register('reestr-conf', ConfirmReestrViewSet, 'reestr-conf')
router.register('reestr-auth', AuthorizedReestrViewSet, 'reestr-auth')
router.register('calculation', Calculation, 'calculation')
router.register('inspection-category', ICCategoryViewSet,
                'inspection-category')
router.register('inspection', InspectionControlViewSet, 'inspection')
router.register('form-category', CategoryDocumentFormViewSet, 'form-category')
router.register('reestr-status', ReestrStatusViewSet, 'reestr-status')
router.register('reestr-tamojnya', RegistriesForTamojnyaViewSet,
                'reestr-tamojnya')
router.register('menu', LanguageViewSet, 'menu')

urlpatterns = [
    path('', include(router.urls)),
]
