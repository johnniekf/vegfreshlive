from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Core
from .models import FoodGroup
from .models import RecipeSet
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Create your views here.

class IndexView(ListView):
    model = Core
    template_name = 'core/index.html'
    context_object_name = 'index'


# Changed references location from 'Core' to 'RecipeIngredients'
class RecipeView(ListView):
    model = Core
    template_name = 'core/recipes.html'
    context_object_name = 'recipe'


class GroupView(ListView):
    model = FoodGroup
    template_name = 'core/category.html'
    context_object_name = 'category'


class SingleView(DetailView):
    model = Core
    template_name = 'core/single.html'
    context_object_name = 'post'


class PostsView(ListView):
    model = Core
    template_name = 'core/admin.html'
    context_object_name = 'post_list'


class AddView(CreateView):
    model = Core
    template_name = 'core/add.html'
    fields = '__all__'
    success_url = reverse_lazy('core:posts')


class EditView(UpdateView):
    model = Core
    template_name = 'core/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:posts')


class Delete(DeleteView):
    model = Core
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:posts')
    template_name = 'core/confirm-delete.html'


class SearchResultView(ListView):
    model = RecipeSet

    template_name = 'core/set_result.html'
    context_object_name = 'recipe_set'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = RecipeSet.objects.filter(
            Q(set_name__exact=query)
        )
        return object_list


@login_required
def dashboard(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save(*args, **kwargs)
            p_form.save(*args, **kwargs)
            messages.success(request, f'Your account has been updated.')
            return redirect('core:dashboard')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'account/dashboard.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save(*args, **kwargs)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('core:index')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
