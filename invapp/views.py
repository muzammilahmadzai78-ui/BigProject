from django.shortcuts import render, redirect
from .models import Product, Profile
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models import Sum
from django.core.paginator import Paginator



# home_view
@login_required
def home(request):
    return render(request, 'invapp/home.html')




# create_view

@login_required
def create_home_view(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            form.save()
            return redirect('product_list')

    return render(request, 'invapp/product_form.html', {'form': form})


@login_required
def create_product_detail(request, product_id):
    product = Product.objects.get(product_id=product_id, user=request.user)
    return render(request, 'invapp/detail.html', {'product': product})
        


# read_view
@login_required
def create_read_view(request):
    search = request.GET.get('search')
    sort = request.GET.get('sort')
    category = request.GET.get('category')
    products = Product.objects.filter(user=request.user)
    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(sku__icontains=search)
        )
    if sort:
        products = products.order_by(sort)
    if category:
        products = products.filter(category=category)
    paginator = Paginator(products, 2)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    current_page = products.number
    start = max(1, current_page -2)
    end = min(products.paginator.num_pages, current_page + 2)
    page_number = range(start, end + 1)
    return render(request, 'invapp/product_list.html', {'products': products, 'page_numbers': page_number})





#update_view
@login_required
def create_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id, user=request.user)
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invapp/product_form.html', {'form': form})


# delete_view
@login_required
def create_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id, user=request.user)

    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'invapp/product_confirm_delete.html')

def register_account(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        form1 = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and form1.is_valid():
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone_number = form1.cleaned_data.get('phone_number')
            image = form1.cleaned_data.get('image')
            user = User.objects.create_user(password=password,
                        username=username, 
                        first_name=first_name,
                        last_name=last_name,
                        email=email)
            Profile.objects.create(
                user = user,
                phone_number = phone_number,
                image = image
            )
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
        form1 = ProfileForm()
    return render(request, 'invapp/register.html', {'form': form, 'form1': form1})




def login_view(request):
    if request.method == "POST":
            password = request.POST.get('password')
            username = request.POST.get('username')
            user = authenticate(request, password=password, username=username)
            if user is not None: 
                login(request, user)
                return redirect('home')

    return render(request, 'invapp/login.html')

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return redirect('home')


def create_user_profile(request):
    search = request.GET.get('search')
    products = Product.objects.filter(user=request.user)
    profiles = Profile.objects.get(user=request.user)
    if search:
        products = Product.objects.filter(
            Q(name__icontains=search) |
            Q(sku__icontains=search)
        )

        
    total_product = products.count()
    total_quantity = products.aggregate(total=Sum('quantity'))['total']
    user = request.user
    return render(request, 'invapp/profile.html', {'total_product': total_product, 
                                                   'total_quantity': total_quantity,
                                                    'products': products,
                                                    'profiles': profiles})