from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Genre
from django.core.paginator import Paginator


def main(request, page=1):
    games = Game.objects.all()
    genres = Genre.objects.all().order_by('name')
    per_page = 48
    paginator = Paginator(list(games), per_page)
    games_on_page = paginator.page(page)
    return render(request, 'shop_app/index.html', context={'games':games_on_page, 'genres': genres})


def game_detail(request, game_title):
    game = get_object_or_404(Game, title=game_title)
    return render(request, 'shop_app/game_detail.html', context={'game_detail': game})


def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    games = genre.game_set.all()  # Получите список игр, связанных с выбранным жанром
    if not games:
        return render(request, 'shop_app/genre_none.html')
    return render(request, 'shop_app/genre_detail.html', {'genre': genre, 'games': games})


def search_results(request):
    query = request.GET.get('q')
    results = Game.objects.filter(title__icontains=query)  # Ищем игры, в названии которых есть текст из запроса
    return render(request, 'shop_app/search_results.html', {'results': results})

