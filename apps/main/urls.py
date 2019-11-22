from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views.doc_parents import DocParentViewSet, DocTypeViewSet
from main.views.file import FileViewSet
from main.views.reestr_info import ReestrInfoUserViewSet
from main.views.static_pages import StaticPagesViewSet
from main.views.user import UserViewSet
from main.views.news import NewsViewSet
from main.views.media import MediaViewSet
from main.views.region import RegionViewSet
from main.views.articles import ArticlesViewSet
from main.views.sliders import SliderViewSet
from main.views.review import ReviewViewSet
from main.views.documents import DocumentViewSet
from main.views.questions import QuestionViewSet
from main.views.employees import EmployeeViewSet
from main.views.registries import RegistriesViewSet
from main.views.type_organ import TypeOrganViewSet
from main.views.laws import LawsViewSet,LawsCategoryViewSet

router = DefaultRouter()
router.register('', UserViewSet, 'user')
router.register('file', FileViewSet, 'file')
router.register('doc-parent', DocParentViewSet, 'doc-parent')
router.register('doc-type', DocTypeViewSet, 'doc-type')
router.register('news', NewsViewSet, 'news')
router.register('media', MediaViewSet, 'media')
router.register('static-pages', StaticPagesViewSet, 'static-pages')

router.register('region', RegionViewSet, 'region')
router.register('articles', ArticlesViewSet, 'articles')
router.register('reviews', ReviewViewSet, 'reviews')
router.register('sliders', SliderViewSet, 'sliders')
router.register('documents', DocumentViewSet, 'documents')
router.register('questions', QuestionViewSet, 'questions')
router.register('employees', EmployeeViewSet, 'employees')
router.register('type-organ', TypeOrganViewSet, 'type-organ')
router.register('laws', LawsViewSet, 'laws')
router.register('laws-category', LawsCategoryViewSet, 'laws-category')
router.register('registries', RegistriesViewSet, 'registries')
router.register('reestr-info', ReestrInfoUserViewSet, 'reestr-info')

urlpatterns = [
    path('', include(router.urls)),
]
