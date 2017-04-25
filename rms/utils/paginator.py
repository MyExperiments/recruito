from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CustomPaginator():
    def __init__(self):
        pass

    def paginate(self, objects, *args, **kwargs):
        paginator = Paginator(objects, kwargs['per_page'])

        try:
            objects = paginator.page(kwargs['page'])
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)

        return objects
