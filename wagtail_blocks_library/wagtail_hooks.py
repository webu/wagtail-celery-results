from django.utils.translation import gettext_lazy as _

from django_celery_results.models import GroupResult
from django_celery_results.models import TaskResult
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.snippets.views.snippets import SnippetViewSetGroup


class TaskResultViewSet(SnippetViewSet):
    model = TaskResult
    menu_icon = "mail"  # Wagtail icon
    menu_label = _("Celery Tasks")

    list_display = ["task_id", "task_name", "status", "date_created"]
    search_fields = ["task_id", "task_name", "result"]
    list_filter = ["status", "task_name", "date_created"]


class GroupResultViewSet(SnippetViewSet):
    model = GroupResult
    menu_icon = "mail"  # Wagtail icon
    menu_label = _("Celery Group")


class CeleryGroupViewSet(SnippetViewSetGroup):
    menu_label = _("Async tasks")
    menu_icon = "tasks"
    menu_order = 480
    items = [TaskResultViewSet, GroupResultViewSet]


register_snippet(CeleryGroupViewSet)
