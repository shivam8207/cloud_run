from django.shortcuts import render, redirect
from .models import Product

def product_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")

        Product.objects.create(
            name=name,
            price=price,
            quantity=quantity
        )

        return redirect("/")

    products = Product.objects.all().order_by("-created_at")

    return render(request, "product.html", {"products": products})

