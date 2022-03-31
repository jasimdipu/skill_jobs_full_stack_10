from django.shortcuts import render

from .models import Category, Product


# Create your views here.
# select * from category, Category.objects.all()

# select all data
# def categories(request):
#     categories = Category.objects.all()

#     context = {
#         'categories': categories,
#     }

#     print(categories)
#     print(categories.query)
#     return render(request, 'index.html', context)

# # where clause orm
# def select_category(request):
#     category = Category.objects.filter(name__startswith = "Woman")
#     print(category)
#     print(category.query)
#     # print(connection.query)


#     return render(request, 'index.html', {'category': category})

def products(request):
    product = Product.objects.filter(name__startswith="vegetable") | Product.objects.filter(slug__startswith='burger')
    print(product.query)
    return render(request, 'index.html', {'products': product})


def product_union_with_category(request):
    product = Product.objects.all().values_list("name").union(Category.objects.all().values_list("name"))
    print(product)
    print(product.query)
    return render(request, 'index.html', {'products': product})


def not_product(request):
    p = Product.objects.exclude(price__gt = 54.00)
    print(p)
    print(p.query)
    return render(request, 'index.html', {'p': p})

# orm selec query, where clause filter values, and or not