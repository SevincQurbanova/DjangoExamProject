# translation.py

from modeltranslation.translator import translator, TranslationOptions
from .models import Position, Department

class PositionTranslationOptions(TranslationOptions):
    fields = ('name',)

class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Position, PositionTranslationOptions)
translator.register(Department, DepartmentTranslationOptions)

# from modeltranslation.translator import translator, TranslationOptions
# from .models import Department, Position

# class DepartmentTranslationOptions(TranslationOptions):
#     fields = ('name',)

# class PositionTranslationOptions(TranslationOptions):
#     fields = ('name',)

# translator.register(Department, DepartmentTranslationOptions)
# translator.register(Position, PositionTranslationOptions)
