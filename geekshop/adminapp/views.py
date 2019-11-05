from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminapp.forms import AdminShopUserUpdateForm, AdminShopUserCreateForm, AdminProductCategoryUpdateForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    context = {
        'title': 'пользователи',
        'shop_users': ShopUser.objects.all().order_by('-is_active', '-is_superuser')
    }
    return render(request, 'adminapp/index.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        form = AdminShopUserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        form = AdminShopUserCreateForm()

    context = {
        'title': 'пользователи/создание',
        'form': form
    }
    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        form = AdminShopUserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        form = AdminShopUserUpdateForm(instance=user)

    context = {
        'title': 'пользователи/редактирование',
        'form': form
    }
    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    user.is_active = False
    user.save()
    # user.delete()
    return HttpResponseRedirect(reverse('myadmin:index'))


@user_passes_test(lambda u: u.is_superuser)
def productcategories(request):
    context = {
        'title': 'категории продуктов',
        'object_list': ProductCategory.objects.all()
    }
    return render(request, 'adminapp/productcategory_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def productcategory_create(request):
    if request.method == 'POST':
        form = AdminProductCategoryUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:productcategories'))
    else:
        form = AdminProductCategoryUpdateForm()

    context = {
        'title': 'категории продуктов/создание',
        'form': form
    }
    return render(request, 'adminapp/productcategory_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def productcategory_update(request, pk):
    obj = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = AdminProductCategoryUpdateForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:productcategories'))
    else:
        form = AdminProductCategoryUpdateForm(instance=obj)

    context = {
        'title': 'категории продуктов/редактирование',
        'form': form
    }
    return render(request, 'adminapp/productcategory_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def productcategory_delete(request, pk):
    obj = get_object_or_404(ProductCategory, pk=pk)
    obj.is_active = False
    obj.save()
    # user.delete()
    return HttpResponseRedirect(reverse('myadmin:productcategories'))
