from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home(request):

    context = {
        "username": "Omid",
        "age": "28",
        "job": "DevOps",
        "articles": [
            {
                "title": "How to Create an Index in Django Without Downtime",
                "description": "Managing database migrations is a great challenge in any software project. Luckily, as of version 1.7, Django comes with a built-in migration framework. The framework is very powerful and useful in managing change in databases. But the flexibility provided by the framework required some compromises. To understand the limitations of Django migrations, you are going to tackle a well known problem: creating an index in Django with no downtime.",
                "img": "https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/How-to-Create-An-Index-Concurrently-in-Django_Watermarked.943163f9806b.jpg&w=960&sig=198548ee34a2d702597a5cda33a941bf5fdee54e",
            },
            {
                "title": "Make a Location-Based Web App With Django and GeoDjango",
                "description": "Throughout this tutorial, you’ll learn how to use Django and GeoDjango to build a location-based web application from scratch. You’ll be building a simple nearby shops application that lists the shops closest to a user’s location. ",
                "img": "https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/Creating-A-Location-Based-Web-Application-with-Django-GeoDjango-and-Postgis_Watermarked.2cb08acd38d4.jpg&w=960&sig=81e0373cc635b2f9afe7641da5c0db5469c94e14",
            },
            {
                "title": "Django Migrations: A Primer",
                "description": "Since version 1.7, Django has come with built-in support for database migrations. In Django, database migrations usually go hand in hand with models: whenever you code up a new model, you also generate a migration to create the necessary table in the database. However, migrations can do much more.",
                "img": "https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/Django-Migrations---A-Primer-Update_Watermarked.798eade8f3df.jpg&w=960&sig=437fc8b66bb0d3fa36f3cce6cb6b8a7fb72aa78a",
            }
        ]
    }

    return render(request, "blog/home.html", context)

def api(request):

    apidata = {
        "1": {
            "title": "Article One",
            "id": "10",
            "slug": "first-article",
        },
        "2": {
            "title": "Article Two",
            "id": "11",
            "slug": "second-article",
        },
        "3": {
            "title": "Article Three",
            "id": "12",
            "slug": "third-article",
        }
    }

    return JsonResponse(apidata)