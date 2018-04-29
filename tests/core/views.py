from django.views.generic.list import ListView
from import_export import views
from . import models


class CategoryExportView(views.ExportViewFormMixin, ListView):
    model = models.Category
