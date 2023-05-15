from django.shortcuts import render
from django.contrib import messages
import openai


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
