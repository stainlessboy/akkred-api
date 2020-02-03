from modeltranslation.translator import TranslationOptions, translator

from main.models.static_pages import StaticPage
from main.models.news import News
from main.models.media import Media
from main.models.review import Review
from main.models.questions import Question
from main.models.employees import Employee
from main.models.laws import Laws
from main.models.type_organ import TypeOrgan
from main.models.sliders import Slider
from main.models.documents import Document, DocumentForm
from main.models.documens_parent import DocParent
from main.models.documents_type import DocType
from main.models.inspection_control import InspectionControl, ICCategory


class StaticPagesTranslation(TranslationOptions):
    fields = ('name', 'body')
    default_translate = False


class NewsMedia(TranslationOptions):
    fields = ('title', 'text')
    default_translate = False


class Medias(TranslationOptions):
    fields = ('title', 'description')
    default_translate = False


class Reviews(TranslationOptions):
    fields = ('author', 'author', 'description')
    default_translate = False


class QA(TranslationOptions):
    fields = ('question', 'answer')
    default_translate = False


class Employer(TranslationOptions):
    fields = ('name', 'position', 'description')
    default_translate = False


class Lawss(TranslationOptions):
    fields = ('name', 'name2', 'link')
    default_translate = False


class TypeOrgans(TranslationOptions):
    fields = ['name']
    default_translate = False


class Sliders(TranslationOptions):
    fields = ['title']
    default_translate = False


class Documents(TranslationOptions):
    fields = ['name', 'description']
    default_translate = False


class DocumentForms(TranslationOptions):
    fields = ['title']
    default_translate = False


class DocParents(TranslationOptions):
    fields = ['name']
    default_translate = False


class DocTypes(TranslationOptions):
    fields = ['name']
    default_translate = False


class InspectionControls(TranslationOptions):
    fields = ['name']
    default_translate = False


class ICCategorys(TranslationOptions):
    fields = ['name']
    default_translate = False


translator.register(StaticPage, StaticPagesTranslation)
translator.register(Media, Medias)
translator.register(News, NewsMedia)
translator.register(Review, Reviews)
translator.register(Question, QA)
translator.register(Employee, Employer)
translator.register(Laws, Lawss)
translator.register(TypeOrgan, TypeOrgans)
translator.register(Slider, Sliders)
translator.register(Document, Documents)
translator.register(DocumentForm, DocumentForms)
translator.register(DocParent, DocParents)
translator.register(DocType, DocTypes)
translator.register(InspectionControl, InspectionControls)
translator.register(ICCategory, ICCategorys)
