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
            ids = []
            for permiso in permisos:
                ids.append(permiso.id_solicitud)
            print(ids)

            result_list = []
            index_list = []

            count_dict = {}

            for index, item in enumerate(ids):
                if item in count_dict:
                    count_dict[item][0] += 1
                    count_dict[item][1].append(index)
                else:
                    count_dict[item] = [1,[index]]

            for item, (count,indices) in count_dict.items():
                if count > 1:
                    result_list.extend([(item,) * count])
                    if len(indices) > 1:
                        index_list.append(tuple(indices))

            print(result_list)

            print(index_list)

            combined_list = []
            for i, permiso in enumerate(permisos):
                materias = []
                materias = [(permiso.materia,permiso.horaInicio,permiso.horaFin,permiso.fecha)]
                for ind,j in enumerate(index_list):
                    if i == j[0]:
                        auxPermisos = RegistroPermisos.objects.filter(id_solicitud = result_list[ind][0],estado='pendiente')
                        
                        materias = []
                        for auxPermiso in auxPermisos:
                            materias.append((auxPermiso.materia,auxPermiso.horaInicio,auxPermiso.horaFin,auxPermiso.fecha))
                        
                    

                combined_list.append((permiso, permiso.project, materias))
            print((len(combined_list),len(permisos)))
            index_list.sort(reverse=True)

            for i in index_list:
                del combined_list[i[1]]
            print((len(combined_list),len(permisos)))


            

            return render(request, 'petitions/petition_list.html', {'permisos': combined_list})
        else:
            return render(request, 'petitions/not_authorized.html')


# Create your views here.

@user_passes_test(admin_user_check, login_url='/login/')
def petition_list(request):
    permisos = RegistroPermisos.objects.filter(estado='pendiente')
    ids = []
    for permiso in permisos:
        ids.append(permiso.id_solicitud)
    print(ids)

    result_list = []
    index_list = []

    count_dict = {}

    for index, item in enumerate(ids):
        if item in count_dict:
            count_dict[item][0] += 1
            count_dict[item][1].append(index)
        else:
            count_dict[item] = [1,[index]]

    for item, (count,indices) in count_dict.items():
        if count > 1:
            result_list.extend([(item,) * count])
            if len(indices) > 1:
                index_list.append(tuple(indices))

    print(result_list)

    print(index_list)

    combined_list = []
    for i, permiso in enumerate(permisos):
        materias = []
        materias = [(permiso.materia,permiso.horaInicio,permiso.horaFin,permiso.fecha)]
        for ind,j in enumerate(index_list):
            if i == j[0]:
                auxPermisos = RegistroPermisos.objects.filter(id_solicitud = result_list[ind][0],estado='pendiente')
                
                materias = []
                for auxPermiso in auxPermisos:
                    materias.append((auxPermiso.materia,auxPermiso.horaInicio,auxPermiso.horaFin,auxPermiso.fecha))
                
            

        combined_list.append((permiso, permiso.project, materias))
    print((len(combined_list),len(permisos)))
    index_list.sort(reverse=True)

    for i in index_list:
        del combined_list[i[1]]
    print((len(combined_list),len(permisos)))


    

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
