from django.shortcuts import render
from.models import Products
from django.core.paginator import Paginator

# Create your views here.


def index(request):
# search code

    product_objects=Products.objects.get_queryset().order_by('id')

    item_name=request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        product_objects=product_objects.filter(title=item_name)
#  paginator code

    paginator=Paginator(product_objects,4)
    page=request.GET.get('page')
    product_objects=paginator.get_page(page)

    return render(request,'index.html',{'product_objects':product_objects})

def detail(request,id):
    product_detail=Products.objects.get(id=id)
    return render(request,'detail.html',{'product_detail':product_detail})

