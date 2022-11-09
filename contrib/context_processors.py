from movies.models import Movie


def sidebar(request): # noqa
    return {"sidebar": Movie.objects.filter(continued=True)[:3]}
