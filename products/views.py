from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from products.models import Product




def searchproducts(request):
    pro = Product.objects.all()


    name = None
    desc = None
    pfrom = None
    pto = None
    cs = None


    if 'cs' in request.GET:
        cs = request.GET['cs']
        if not cs:
            cs = 'off'

    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            if cs=='on':
                pro = pro.filter(name__contains=name)
            else:
                pro = pro.filter(name__icontains=name)
                

    if 'searchdesc' in request.GET:
        desc = request.GET['searchdesc']
        if desc:
            if cs=='on':
                pro = pro.filter(description__contains=desc)
            else:
                pro = pro.filter(description__icontains=desc)


        
    if 'searchfrom' in request.GET and 'searchto' in request.GET:
        pfrom = request.GET['searchfrom']
        pto = request.GET['searchto']
        if pfrom and pto:
            if pfrom.isdigit() and pto.isdigit():
                pro = pro.filter( price__gte=pfrom , price__lte=pto )
        



    context = {
        'products':pro
    }
    return render( request , 'products/searchproducts.html' , context  )




def products(request):
    context = {
        'products':Product.objects.all()
    }
    return render( request , 'products/products.html' , context )



def product(request, pro_id):
    context = {
        'pro':get_object_or_404(Product, pk=pro_id)
    }
    return render( request , 'products/product.html', context )



def advancedsearch (request):
    return render( request , 'products/advancedsearch.html' )

