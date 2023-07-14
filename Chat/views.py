from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MensajeForm
from .models import Mensaje, Conversacion
from django.contrib.auth.models import User


@login_required()
def chatView(request):
    form = MensajeForm()
    return render(request, "chat/templatePadreChat.html", {'form': form})


# Mensajes ------------------------------------------------------------------------------------------------------------------


@login_required()
def listaMensajes(request):
    pass


@login_required()
def enviarMensajes(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            receptor_id = request.POST.get('receptor_id')
            contenido = form.cleaned_data['contenido']
            emisor = request.user  # Obtener el usuario emisor
            receptor = User.objects.get(id=receptor_id)  # Obtener el usuario receptor usando el ID

            mensaje = Mensaje(emisor=emisor, receptor=receptor, contenido=contenido)
            mensaje.save()
            return redirect('chat:listaConversaciones')  # Redirigir a la lista de conversaciones

    else:
        form = MensajeForm()

    return render(request, "chat/templatePadreChat.html", {'form': form})


@login_required()
def buscarMensajes(request):
    pass


@login_required()
def eliminarMensajes(request):
    pass





# Conversaciones ------------------------------------------------------------------------------------------------------------------


def listaConversaciones(request):
    pass

@login_required()
def buscarConversaciones(request):
    pass


@login_required()
def eliminarConversaciones(request):
    pass

