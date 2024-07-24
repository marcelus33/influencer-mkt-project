from django.views.generic import ListView

from content.models import Content


class HomeView(ListView):
    template_name = 'home.html'
    model = Content
    context_object_name = 'contents'
    paginate_by = 30

    def get_queryset(self):
        return Content.objects.select_related('creator').all()


class FilteredContentListView(ListView):
    model = Content
    template_name = 'partials/content_list.html'
    context_object_name = 'contents'
    paginate_by = 30

    def get_queryset(self):
        platform = self.request.GET.get('platform', "all")
        if platform == "all":
            queryset = Content.objects.select_related('creator').all()
        else:
            queryset = Content.objects.select_related('creator').filter(creator__platform=platform)
        return queryset
