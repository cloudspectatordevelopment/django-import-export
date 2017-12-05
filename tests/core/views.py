from django.views.generic.list import ListView
from import_export import views
from . import models


class CategoryExportView(views.ExportViewMixin, ListView):
    model = models.Category
