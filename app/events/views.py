from django.views.generic import ListView, DetailView, View, TemplateView
from django.db.models.functions import TruncDay
from .models import Event, DayEvent
from django.http import HttpResponse, JsonResponse, Http404
import datetime 
from django.db.models import ExpressionWrapper, DateField
from django.utils.timezone import make_aware

class DayEventsListView(ListView):
    template_name = "events/events.html"
    # model = DayEvent

    def get_queryset(self):
        # return Event.objects.upcoming().annotate(day=TruncDay('start_at'))
        return DayEvent.objects.upcoming().annotate(day=TruncDay('start_at'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LAYOUT'] = 'NORMAL'
        return context


class GetDayEventListView(TemplateView):
    """
    Возвращает отрендеренный список мероприятий в заданный день в ответ на ajax запрос.
    Используется в плагине "Календарь мероприятий"
    """

    template_name = "events/includes/event_list.html"

    def get(self,request, *args, **kwargs):
        # пропускаем только ajax запросы
        if not request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            raise Http404

        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        date = self.request.GET.get("date", "")
        try:
            date = make_aware(datetime.datetime.strptime(date, "%Y-%m-%d")).date()
        except ValueError:
            raise Http404

        # список меропиятий в заданный день
        qs = DayEvent.objects.upcoming_by_date(date)

        category_id = self.request.GET.get("event-category", None)
        if category_id and category_id.isdigit():
            qs = qs.filter(category=category_id)
        
        qs = qs.annotate(day=TruncDay('start_at'))

        context['object_list'] = qs
        context['LAYOUT'] = 'SMALL'
        context['date'] = date

        return context
    