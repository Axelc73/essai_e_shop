from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.hashers import make_password, check_password
from store.views import index

def signup(request):
    log = 'non'
    Shopper = get_user_model()
    if request.method == 'POST':
        # Récupérer les données du formulaire
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

            # Vérifier que les mots de passe correspondent
        if password1 != password2:
            log = 'Les mots de passe ne correspondent pas.'
        else:
            try:
                # Vérifier si un utilisateur avec le même nom d'utilisateur existe
                user = Shopper.objects.get(username=username)

                # Vérifier si l'email et le mot de passe correspondent
                if user.email == email and check_password(password1, user.password):
                    # Connecter l'utilisateur
                    login(request, user)
                    return redirect('index')
                else:
                    log = 'Nom d\'utilisateur ou mot de passe incorrect.'
            except Shopper.DoesNotExist:
                if Shopper.objects.filter(username=username).exists():
                    log = 'Nom d\'utilisateur déjà pris.'
                elif Shopper.objects.filter(email=email).exists():
                    log = 'Email déjà utilisé.'
                else:
                    # Créer un nouvel utilisateur
                    user = Shopper.objects.create(
                    username=username,
                    email=email,
                    password=make_password(password1)  # Hacher le mot de passe
                )
                # Connecter l'utilisateur
                login(request, user)
                return redirect('index')
    return render(request, 'accounts/signup.html', context={'log': log})
