from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product

def index_view(request):
    return render(request, 'index.html')

def cart(request):
    # cart ビューのロジック
    return render(request, 'cart.html')
  
def item(request):
    products = Product.objects.all()
    for product in products:
        product.price = int(product.price)  # 価格を整数に変換
    return render(request, 'item.html', {'products': products})
  
def camp(request):
    # camp ビューのロジック
    return render(request, 'camp.html')  

def new(request):
    # new ビューのロジック
    return render(request, 'new.html')  
  
def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {'product': product})
     
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    images = product.images.all()  # 特定の商品に関連するすべての画像を取得
    return render(request, 'detail.html', {'product': product, 'images': images})
