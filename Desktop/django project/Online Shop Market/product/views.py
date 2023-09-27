from django.shortcuts import render
from django.views.generic import TemplateView
from .models import*
from .forms import *
from django.shortcuts import redirect
import random
import numpy as np

import random




def Home(requests):
    ctg = Category.objects.all()
    sneaker = Sneakers.objects.all()
    advertising = Advertising.objects.all()
    random_sneak = random.choice(advertising)
    image = Image.objects.all()
    feel = Feel.objects.all()
    ctx = {
        'ctg':ctg,
        'Sneaker': sneaker,
        'random_sneak': random_sneak,
        'image': image,
        'feel': feel
    }
    return render(requests, "blog/index.html", ctx)

def Contact(requests):
    ctx = {}
    return render (requests, "blog/contact.html", ctx)

def Product(requests, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    sneaker = Sneakers.objects.all().filter(type_id=category.id)
    ctx = {
        'ctg': ctg,
        'category': category,
        'sneaker': sneaker
    }
    return render (requests, "blog/products.html", ctx)

def Register(requests):
    ctx = {}
    return render (requests, "blog/register.html", ctx)


def Single(requests, pk=None):
    ctg = Category.objects.all()
    products_pk = Sneakers.objects.get(pk=pk)
    sneakers = Sneakers.objects.all()
    random_s = random.choices(sneakers, k=3)

    form = ChoiceForm()
    if requests.POST:
        forms = ChoiceForm(requests.POST or None,
                           requests.FILES or None)
        if forms.is_valid():
            root = forms.save()
            root = Buy.objects.get(pk=root.id)
            root.product = products_pk
            root.save()
            return redirect("home")
        else:
            print(forms.errors)
    ctx = {
        "ctg":ctg,
        "product_pk":products_pk,
        "form": form,
        'random_s': random_s,
        'sneakers': sneakers,
    }
    return render (requests, "blog/single.html", ctx)

# class HomePage(ListView):
#     template_name = "blog/index.html"
#     model = Category



# class Contact(ListView):
#     template_name = "blog/contact.html"
#     model = Category



# class Product(ListView):
#     template_name = "blog/products.html"
#     model = Category
#     # model = Sneakers

# class Register(ListView):
#     template_name = "blog/register.html"
#     model = Category

# class Single(ListView):
#     template_name = "blog/single.html"
#     model = Category


# Create your views here.
