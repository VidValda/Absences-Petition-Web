from django.shortcuts import render, HttpResponse, redirect
from .models import Petition
from .forms import PetitionForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View  # Import the View class
from django.http import JsonResponse

def admin_user_check(user):
    return user.is_authenticated and user.is_staff



class AdminOnlyView(LoginRequiredMixin, View):
    login_url = '/login/'  

    def get(self, request):
        if request.user.is_staff:  # Additional check for admin users
            petitions = Petition.objects.filter(status='pending')
            return render(request, 'petitions/petition_list.html', {'petitions': petitions})
        else:
            return render(request, 'petitions/not_authorized.html')


# Create your views here.

@user_passes_test(admin_user_check, login_url='/login/')
def petition_list(request):
    petitions = Petition.objects.filter(status='pending')
    return render(request, 'petitions/petition_list.html', {'petitions': petitions})


def update_petition_status(request, petition_id, new_status):
    petition = Petition.objects.get(pk=petition_id)

    if request.method == 'POST':
        if new_status == 'accepted' or new_status == 'declined':
            form = PetitionForm(request.POST, instance=petition)
            if form.is_valid():
                if new_status == 'accepted' or new_status == 'declined':
                    petition.status = new_status
                    petition.observations = form.cleaned_data['observations']
                    petition.save()
                    return redirect('petition_list')
        else:
            return redirect('petition_list')
    else:
        form = PetitionForm(instance=petition)

    return render(request, 'petitions/update_petition.html', {'form': form, 'petition': petition, 'new_status': new_status})


def create_petition(request):
    if request.method == 'POST':
        form = PetitionForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()
            return redirect('create_petition')
    else:
        form = PetitionForm()
    return render(request, 'petitions/create_petition.html', {'form': form})


def update_observation(request):
    if request.method == 'POST':
        petition_id = request.POST.get('petition_id')
        observation = request.POST.get('observation')

        # Perform the update operation on your model based on the petition_id and observation
        # Example: You can use the petition_id to retrieve the corresponding model instance and update the observation field.

        # Return a JSON response to indicate success
        return JsonResponse({'message': 'Observation updated successfully'})
    else:
        # Handle other HTTP methods if necessary
        return JsonResponse({'error': 'Invalid request method'}, status=405)
