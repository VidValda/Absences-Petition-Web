from django.shortcuts import render, HttpResponse, redirect
from .models import RegistroPermisos,RegistroEstudiantes
from .forms import RegistroPermisosForm, RegistroEstudiantesForm
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
            permisos = RegistroPermisos.objects.filter(estado='pendiente')
     
            combined_list = [(permiso, permiso.project) for permiso in permisos]
            return render(request, 'petitions/petition_list.html', {'permisos': combined_list})
        else:
            return render(request, 'petitions/not_authorized.html')


# Create your views here.

@user_passes_test(admin_user_check, login_url='/login/')
def petition_list(request):
    permisos = RegistroPermisos.objects.filter(estado='pendiente')
    combined_list = [(permiso, permiso.project) for permiso in permisos]

    return render(request, 'petitions/petition_list.html', {'permisos': combined_list})


def update_petition_status(request, permiso_id, new_status):
    permiso = RegistroPermisos.objects.get(pk=permiso_id)

    if request.method == 'POST':
        
        if new_status == 'aceptado' or new_status == 'rechazado':
            form = RegistroPermisosForm(request.POST, instance=permiso)
            print(new_status)
            permiso.estado = new_status
            permiso.save()
            return redirect('petition_list')
        
        else:
            return redirect('petition_list')
    else:
        form = RegistroPermisosForm(instance=permiso)

    return render(request, 'petitions/update_petition.html', {'form': form, 'petition': permiso, 'new_status': new_status})


def create_petition(request):
    if request.method == 'POST':
        form = RegistroPermisosForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()
            return redirect('create_petition')
    else:
        form = RegistroPermisosForm()
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
