from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import prob5_the_anikanik_girls

def home(request):
	records = prob5_the_anikanik_girls.objects.all()


	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		#Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Congrats, gastador!")
			return redirect('home')
		else:
			messages.success(request, "Bili ka pa nang marami!")
			return redirect('home')

	else:
		return render(request, 'home.html', {'records':records})


def logout_user(request):
	logout(request)
	messages.success(request, "Congrats, gastador!")
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Bili ka pa nang marami!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def prob5_the_anikanik_girls_record(request, pk):
	if request.user.is_authenticated:
			#Look Up Records
			prob5_the_anikanik_girls_record = prob5_the_anikanik_girls.objects.get(id=pk)
			return render(request, 'record.html', {'prob5_the_anikanik_girls_record':prob5_the_anikanik_girls_record})
	else:
		messages.success(request, "More gastos on its way!")
		return redirect('home')


def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = prob5_the_anikanik_girls.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Congrats, gastador!")
		return redirect('home')
	else:
		messages.success(request, "More gastos on its way!")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Congrats, gastador!")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "More gastos on its way!")
		return redirect('home')	


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = prob5_the_anikanik_girls.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Congrats, gastador!")
			return redirect('home')	
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "More gastos on its way!")
		return redirect('home')	