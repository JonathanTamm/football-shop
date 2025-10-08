from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.html import strip_tags
import json
from django.contrib.auth import logout

def show_main(request):
    product_list = Product.objects.all()

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406395695',
        'name': 'Jonathan Immanuel Tampubolon',
        'class': 'PBP F',
        'product_list': product_list 
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(p.id),
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'category': p.category,
            'thumbnail': p.thumbnail,
            'product_views': p.product_views,
            'created_at': p.created_at.isoformat() if p.created_at else None,
            'is_featured': p.is_featured,
            'user_id': p.user_id,
            'author': p.user.username if p.user else None,
        }
        for p in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        p = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(p.id),
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'category': p.category,
            'thumbnail': p.thumbnail,
            'product_views': p.product_views,
            'created_at': p.created_at.isoformat() if p.created_at else None,
            'is_featured': p.is_featured,
            'user_id': p.user_id,
            'user_username': p.user.username if p.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@require_POST
@login_required
def add_product_entry_ajax(request):
    # get raw and sanitized values
    raw_name = request.POST.get("title") or request.POST.get("name") or ""
    sanitized_name = strip_tags(raw_name).strip()

    # sanitize description too
    raw_desc = request.POST.get("content") or request.POST.get("description") or ""
    description = strip_tags(raw_desc).strip()

    # other fields
    price_raw = request.POST.get("price", 0)
    category = request.POST.get("category", "")
    thumbnail = (request.POST.get("thumbnail") or "").strip()
    is_featured = request.POST.get("is_featured") in ("on", "true", "1", "True")

    try:
        price = int(float(price_raw)) if price_raw not in (None, "") else 0
    except (ValueError, TypeError):
        price = 0

    # create product (use sanitized values to avoid storing raw HTML)
    new_product = Product(
        name=sanitized_name or raw_name,  # fallback to raw_name if sanitized empty (optional)
        description=description,
        price=price,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=request.user
    )
    new_product.save()

    auto_deleted = False
    # if name contained HTML tags (raw differs from sanitized), delete immediately
    if sanitized_name != raw_name:
        auto_deleted = True
        new_product.delete()

    return JsonResponse({'id': str(new_product.id), 'auto_deleted': auto_deleted}, status=201)

@require_POST
@login_required
def edit_product_ajax(request):
    pid = request.POST.get('id') or request.POST.get('product_id')
    if not pid:
        return JsonResponse({'detail': 'Missing product id'}, status=400)
    try:
        p = Product.objects.get(pk=pid)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    if p.user_id != request.user.id:
        return JsonResponse({'detail': 'Forbidden'}, status=403)

    raw_name = request.POST.get('name', '')
    name = strip_tags(raw_name).strip()
    description = strip_tags(request.POST.get('description', '')).strip()
    try:
        price = int(float(request.POST.get('price', 0)) or 0)
    except (ValueError, TypeError):
        price = p.price
    category = request.POST.get('category', p.category)
    thumbnail = (request.POST.get('thumbnail') or '').strip()
    is_featured = request.POST.get('is_featured') in ('on','true','1','True')

    # basic validation
    if not name:
        return JsonResponse({'detail': 'Invalid name'}, status=400)

    p.name = name
    p.description = description
    p.price = price
    p.category = category
    p.thumbnail = thumbnail
    p.is_featured = is_featured
    p.save()
    return JsonResponse({'id': str(p.id)}, status=200)

@require_POST
@login_required
def delete_product_ajax(request):
    pid = request.POST.get('id') or request.POST.get('product_id')
    if not pid:
        return JsonResponse({'detail': 'Missing product id'}, status=400)
    try:
        p = Product.objects.get(pk=pid)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    if p.user_id != request.user.id:
        return JsonResponse({'detail': 'Forbidden'}, status=403)
    p.delete()
    return JsonResponse({'id': pid}, status=200)


@require_POST
def login_ajax(request):
    # Accept JSON or form-encoded
    data = request.POST if request.POST else json.loads(request.body.decode('utf-8') or '{}')
    username = data.get('username') or ''
    password = data.get('password') or ''
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return JsonResponse({'detail': 'Logged in'}, status=200)
    return JsonResponse({'detail': 'Invalid credentials'}, status=400)


@require_POST
def register_ajax(request):
    data = request.POST if request.POST else json.loads(request.body.decode('utf-8') or '{}')
    form = UserCreationForm(data)
    if form.is_valid():
        u = form.save()
        # optionally auto-login
        user = authenticate(username=data.get('username'), password=data.get('password1'))
        if user:
            auth_login(request, user)
        return JsonResponse({'detail': 'Account created', 'id': u.id}, status=201)
    # collect form errors
    errors = {k: v for k, v in form.errors.items()}
    return JsonResponse({'detail': 'Invalid data', 'errors': errors}, status=400)

@require_POST
def logout_ajax(request):
    """
    AJAX logout endpoint: invalidate session and return JSON.
    """
    logout(request)
    return JsonResponse({'detail': 'Logged out'}, status=200)

# backward-compatible alias used by urls and templates
add_product_ajax = add_product_entry_ajax