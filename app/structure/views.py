from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse, Http404
from .models import Organization, Otdel
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import get_object_or_404

# ACTION_LIST = ("get-otdels", )
# RESULTS = {
#     0 : "error",
#     1 : "success",
# }
# class AdminView(View):

#     def dispatch(self, request, *args, **kwargs):

#         if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
#             return self.ajax_post(request, *args, **kwargs)

#         return super().dispatch(request, *args, **kwargs)
    

#     def ajax_post(self, request, *args, **kwargs):

#         if not request.user.is_authenticated:
#             raise PermissionDenied

#         action = request.POST.get("action")
#         org_id = request.POST.get("org_id")

#         if action not in ACTION_LIST:
#             raise Http404

#         try:
#             org = Organization.objects.get(pk=org_id)
#         except Organization.DoesNotExist:
#             raise Http404
        
#         if org and (action == 'get-otdels'):
#             # try:
#             return self.get_otdels(request, org)
#             # except PermissionDenied:
#                 # return JsonResponse({"result": RESULTS[0], "message": "Нет прав доступа для этой операции"})

#         raise Http404

#     # @method_decorator(permission_required("structure.change_otdel", raise_exception=True))
#     def get_otdels(self, request, org:Organization):
#         '''Switching publish state of Post'''

#         return JsonResponse({"result": RESULTS[1], 
#                              "message": "Данные получены", 
#                              "data": org.get_otdels()})
        # if post.published:
        #     post.published = False
        #     post.save()
        #     return JsonResponse({"result": RESULTS[1], "message": "Снято с публикации"})
        # else:
        #     # if post has child plugins
        #     if CMSPlugin.objects.filter(placeholder_id=post.content_id).count() > 0:
        #         post.published = True
        #         post.save()
        #         return JsonResponse({"result": RESULTS[1], "message": "Опубликовано"})
        #     else: # no child plugins
        #         message = "Новость пуста и поэтому не может быть опубликована. \n Добавьте плагинов на страницу."
        #         return JsonResponse({"result": RESULTS[0], "message": message})


class GetOtdelsView(View):
    """
    Возвращает список отделов в ответ на ajax запрос
    Используется в форме SotrudnikForm
    Обрабатывается в js/sotrudnik_form.js

    https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
    """
    def get(self,request, *args, **kwargs):

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            org_id = request.GET.get("org_id", None)
            if org_id and org_id.isdigit():
                org = get_object_or_404(Organization, id=org_id)
                otdels = Otdel.objects.filter(organization=org).values('id', 'name')
                return JsonResponse({'data': list(otdels)})

        raise Http404
    
class OrganizationListView(ListView):
    template_name = "structure/base.html"
    queryset = Organization.objects.none()