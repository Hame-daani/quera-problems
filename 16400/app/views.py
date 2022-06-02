from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login as auth_login

from django.db.models import Count

from app.models import Movie, Seat, Ticket


def list_movies(request):
    return render(request, "app/movies.html", {"movies": Movie.objects.all()})


def list_seats(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reserved = movie.ticket_set.all().values_list("seat", flat=True)
    seats = Seat.objects.exclude(id__in=reserved)
    return render(request, "app/seats.html", {"movie": movie, "seats": seats})


def reserve_seat(request, movie_id, seat_id):
    if request.user.is_authenticated:
        m = Movie.objects.get(id=movie_id)
        s = Seat.objects.get(id=seat_id)
        u = request.user
        Ticket.objects.create(movie=m, seat=s, user=u)
        return redirect("list_seats", movie_id=movie_id)
    else:
        return redirect(f"/login?next=/movie/{movie_id}/seats")


def stats(request):
    if request.user.is_authenticated and request.user.is_superuser:
        seats = Seat.objects.annotate(count=Count("ticket"))
        res = []
        for s in seats:
            res.append({"seat__number": s.number, "total": s.count})
        return JsonResponse({"stats": res})
    else:
        return HttpResponseForbidden()


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("list_movies")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
