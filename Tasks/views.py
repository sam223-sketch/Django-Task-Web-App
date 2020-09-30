from django import forms # to import forms when added to an app
from django.http import HttpResponseRedirect # import reverse
from django.shortcuts import render
from django.urls import reverse # import reverse




# class of fields for the forms created
class NewTaskForm(forms.Form):
	task = forms.CharField(label="New Task") # add new task
	priority = forms.IntegerField(label="Priority", min_value=1, max_value=10) # select number to set a priority


# this is a function which will allow the html template have complete access to all tasks
def index(request):
	# this allows a different user to have unique session than view what other users tasks listed
	# prevents all users from viewing the same list of tasks
	if "tasks" not in request.session:
		request.session["tasks"] = [] # if user does not have a list it should give the user an empty list of tasks

	return render(request, "Tasks/index.html", {
		"tasks": request.session["tasks"] # this line calls a new session for every new user
		}) 


# add new tasks function
def add(request):
	if request.method == "POST":
		form = NewTaskForm(request.POST) # ALL data will be fed into the form
	
		if form.is_valid():
			task = form.cleaned_data["task"] #will give access to data user submitted
			request.session["tasks"] += [task] # will store and add up new task to the list
			return HttpResponseRedirect(reverse("Tasks:index")) # reverse to a specified url after submitting form
		else:
			return render(request, "Tasks/addtasks.html", {
				"form": form # error check returns back to add task page
				})
		
	return render(request, "Tasks/addtasks.html", {
		"form": NewTaskForm()
	}) #this will give access to avariable called form when task is to be added