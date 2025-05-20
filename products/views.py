from django.shortcuts import render, get_object_or_404
from .models import Product, Category


# products/views.py
from django.views.generic import CreateView
from .forms import ProductForm
from django.urls import reverse_lazy


# products/views.py
from django.views.generic import UpdateView


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product.html', {'product': product})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(active=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    return render(request, 'products/products.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')



class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')




# products/views.py
from django.views.generic import ListView

class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset.filter(active=True)
    

# products/views.py
from django.views.generic import DeleteView

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


# products/views.py
from django.views.generic import DetailView

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'  # We'll create this template next
    context_object_name = 'product'