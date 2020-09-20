from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import NameForm, MobileForm, AddressForm, AddFarmForm, AddWaterResourceForm, AddPlotsForm, AddPlotingForm, AddReportsImageForm
from django.contrib import messages
import requests
from . import service
from user.models import Address, Applications
from farm.models import Farm, Soil, WaterResource, Plots, Ploting, Reports
from django.shortcuts import get_object_or_404


appid = '4190e8f33d3dcb5489def02c650faaea'
city = 'satana'


@login_required
def index(request):
    user = request.user
    profile = request.user.profile
    if user.first_name == '' or user.last_name == '':
        return redirect('profile')
    elif profile.mobile == '':
        return redirect('profile')
    else:
        lists = service.get_wheather(city)
        print(lists)
        return render(request, 'site/user_home.html', {})


@login_required
def become_biologist(request):
    profile = request.user.profile
    applications = Applications.objects.filter(user=request.user, applied_for='2')
    if applications:
        messages.success(request, f'Your application for biologist is already submited and is in processing stage')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        if profile.type == 1:
            application = Applications(user=request.user, applied_for=2)
            application.save()
            messages.success(request, f'Your application for biologist is submited!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif profile.type == 1:
            application = Applications(user=request.user, applied_for=2)
            application.save()
            messages.success(request, f'You are already biologist!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.success(request, f'Something Went Wrong!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    


@login_required
def complete_profile(request):
    template = 'site/user_profile.html'
    if request.method == 'POST':
                name_form = NameForm(
                    request.POST, request.FILES, instance=request.user)
                mobile_form = MobileForm(
                    request.POST, request.FILES, instance=request.user.profile)
                if name_form.is_valid() or mobile_form.is_valid():
                        post = name_form.save()
                        post.save()
                        mobile = mobile_form.save()
                        mobile.save()
                        messages.success(
                            request, f' ' + post.first_name + ' Your profile updated Successfully!')
                        return redirect('user_home')

    else:
        name_form = NameForm(instance=request.user)
        mobile_form = MobileForm(instance=request.user.profile)

    context = {
        'name_form': name_form,
        'mobile_form': mobile_form,
    }
    return render(request, template, context)


@login_required
def add_address(request):
    template = 'site/dashboard/add_address.html'
    if request.method == 'POST':
                form = AddressForm(request.POST or None, request.FILES or None)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.user = request.user
                        post.save()
                        messages.success(request, "Your address has been created")
                        return redirect('add_address')
    else:
        objects = Address.objects.filter(user=request.user)
        form = AddressForm()

    context = {
        'form': form,
        'objects':objects,
    }
    return render(request, template, context)


@login_required
def add_farm(request):
    template = 'site/dashboard/add_farm.html'
    if request.method == 'POST':
                form = AddFarmForm(request.user, request.POST or None, request.FILES or None)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.owner = request.user
                        post.save()
                        messages.success(request, "Your farm has been created")
                        return redirect('user_home')
    else:
        objects = Farm.objects.filter(owner=request.user)
        form = AddFarmForm(request.user)

    context = {
        'form': form,
        'objects':objects,
    }
    return render(request, template, context)


@login_required
def add_water_resource(request):
    template = 'site/dashboard/add_water_resource.html'
    if request.method == 'POST':
                form = AddWaterResourceForm(request.POST or None, request.FILES or None)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.owner = request.user
                        post.save()
                        messages.success(request, "Your farm has been created")
                        return redirect('user_home')
    else:
        objects = WaterResource.objects.filter(owner=request.user)
        form = AddWaterResourceForm()

    context = {
        'form': form,
        'objects':objects,
    }
    return render(request, template, context)


@login_required
def add_plot(request):
    template = 'site/dashboard/add_plot.html'
    if request.method == 'POST':
                form = AddPlotsForm(request.user, request.POST or None, request.FILES or None)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.owner = request.user
                        post.save()
                        messages.success(request, "Your farm has been created")
                        return redirect('user_home')
    else:
        
        objects = Plots.objects.filter(farm__owner=request.user)
        form = AddPlotsForm(request.user)

    context = {
        'form': form,
        'objects':objects,
    }
    return render(request, template, context)


@login_required
def add_ploting(request):
    template = 'site/dashboard/add_ploting.html'
    if request.method == 'POST':
                form = AddPlotingForm(request.POST or None, request.FILES or None)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.owner = request.user
                        post.save()
                        messages.success(request, "Your farm has been created")
                        return redirect('add_ploting')
    else:
        
        objects = Ploting.objects.filter(plot__farm__owner=request.user)
        form = AddPlotingForm()

    context = {
        'form': form,
        'objects':objects,
    }
    return render(request, template, context)



@login_required
def planting_details(request, id=None):
    template = 'site/dashboard/ploting_details.html'
    ploting = get_object_or_404(Ploting, id=id)
    reports = Reports.objects.filter(ploting=ploting)
    context = {
        'reports': reports,
        'ploting':ploting,
    }

    return render(request, template, context)



@login_required
def upload(request):
    if request.method == 'POST':
        form = AddReportsImageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.added_by = request.user
            post.save()
            messages.success(request, f'Post submitted successfully!')
            return redirect("user_home")
    else:
        form = AddReportsImageForm()
   
    return render(request, 'site/dashboard/add_images.html',{'form': form})