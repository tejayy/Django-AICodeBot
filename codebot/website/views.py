from django.shortcuts import render, redirect
from django.contrib import messages
import openai
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Code


# Create your views here.
def home(request):
    # API = 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
    lang_list = [
        "c",
        "clike",
        "coffeescript",
        "cpp",
        "csharp",
        "css",
        "css-extras",
        "dart",
        "django",
        "go",
        "html",
        "java",
        "javascript",
        "markup",
        "markup-templating",
        "matlab",
        "mongodb",
        "objectivec",
        "perl",
        "php",
        "powershell",
        "python",
        "r",
        "regex",
        "ruby",
        "rust",
        "sas",
        "sql",
        "swift",
        "typescript",
        "yaml",
    ]

    if request.method == "POST":
        code = request.POST["code"]
        lang = request.POST["lang"]
        """Chekc to make sure that the language is picked up"""
        if lang == "Select Programming Language":
            messages.success(request, "Hey! You forgot to select a language")
            return render(
                request,
                "home.html",
                {"lang_list": lang_list, "code": code, "lang": lang},
            )
        else:
            """OpenAI Key"""
            openai.api_key = "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"
            """Create OpenAi Instance"""
            openai.Model.list()
            """Make An OpenAi Request"""
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Respond only with code. Fix This {lang} code {code}",
                    temperature=0,
                    max_tokens=1000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                )
                """Parse the response"""
                response = (response["choices"][0]["text"]).strip()

                return render(
                    request,
                    "home.html",
                    {"lang_list": lang_list, "response": response, "lang": lang},
                )

            except Exception as e:
                return render(
                    request,
                    "home.html",
                    {"lang_list": lang_list, "response": e, "lang": lang},
                )

    return render(request, "home.html", {"lang_list": lang_list})


def suggest(request):
    lang_list = [
        "c",
        "clike",
        "coffeescript",
        "cpp",
        "csharp",
        "css",
        "css-extras",
        "dart",
        "django",
        "go",
        "html",
        "java",
        "javascript",
        "markup",
        "markup-templating",
        "matlab",
        "mongodb",
        "objectivec",
        "perl",
        "php",
        "powershell",
        "python",
        "r",
        "regex",
        "ruby",
        "rust",
        "sas",
        "sql",
        "swift",
        "typescript",
        "yaml",
    ]

    if request.method == "POST":
        code = request.POST["code"]
        lang = request.POST["lang"]
        """Chekc to make sure that the language is picked up"""
        if lang == "Select Programming Language":
            messages.success(request, "Hey! You forgot to select a language")
            return render(
                request,
                "suggest.html",
                {"lang_list": lang_list, "code": code, "lang": lang},
            )
        else:
            """OpenAI Key"""
            openai.api_key = "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"
            """Create OpenAi Instance"""
            openai.Model.list()
            """Make An OpenAi Request"""
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Respond only with code. {code}",
                    temperature=0,
                    max_tokens=1000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                )
                """Parse the response"""
                response = (response["choices"][0]["text"]).strip()

                return render(
                    request,
                    "suggest.html",
                    {"lang_list": lang_list, "response": response, "lang": lang},
                )

            except Exception as e:
                return render(
                    request,
                    "suggest.html",
                    {"lang_list": lang_list, "response": e, "lang": lang},
                )

    return render(request, "suggest.html", {"lang_list": lang_list})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in..')
            return redirect('home')
        else:
            messages.success(request, 'Error Loggin In..')
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, 'you have been logged out! Have a nice Day..')
    return redirect('home')
    
def register_user(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Registered...Congrats!!")
			return redirect('home')

	else:
		form = SignUpForm()

	return render(request, 'register.html', {"form": form})


def past(request):
	if request.user.is_authenticated:
		code = Code.objects.filter(user_id=request.user.id)
		return render(request, 'past.html', {"code":code})	
	else:
		messages.success(request, "You Must Be Logged In To View This Page")
		return redirect('home')


def delete_past(request, Past_id):
	past = Code.objects.get(pk=Past_id)
	past.delete()
	messages.success(request, "Deleted Successfully...")
	return redirect('past')
    
    