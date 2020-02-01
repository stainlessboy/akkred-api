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




# title
# text
# photo

# author = mo
# position =
# description
# image = mod

# question
# answer =

# name = mode
# position =
# description

translator.register(StaticPage, StaticPagesTranslation)
translator.register(Media, Medias)
translator.register(News, NewsMedia)
translator.register(Review, Reviews)
translator.register(Question, QA)
translator.register(Employee, Employer)
translator.register(Laws, Lawss)
translator.register(TypeOrgan, TypeOrgans)
translator.register(Slider, Sliders)
