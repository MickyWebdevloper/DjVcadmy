from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def products_all(request):
    """
    Retrieve all active products and render them on the index page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered response containing all active products.
    """
    # products = Product.objects.all()[:5]
    products = Product.products.all()
    return render(request, "store/home.html", {"products": products})


def product_detail(request, slug):
    """
    Retrieve details of a specific product by its slug and render them on the single product page.

    Args:
        request: The HTTP request object.
        slug (str): The slug of the product.

    Returns:
        A rendered response containing the details of the specified product.
    """

    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, "store/products/single.html", {"product": product})


def category_list(request, category_slug):
    """
    Retrieve products belonging to a specific category and render them on the category page.

    Args:
        request: The HTTP request object.
        category_slug (str, optional): The slug of the category to filter products by. Defaults to None.

    Returns:
        A rendered response containing the specified category and its associated products.
    """

    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.filter(category=category)
    return render(
        request,
        "store/products/category.html",
        {"category": category, "product": product},
    )
