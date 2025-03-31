from django.shortcuts import render
from .models import Video, Playlist
from math import ceil as c
import random

# Create your views here.
def video(request):
    no_of_videos = 12
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    videos = Video.objects.all()
    length = len(videos)
    videos = videos[(page-1)*no_of_videos: page*no_of_videos]
    if page > 1:
        prev = page-1
    else:
        prev = None
    if page < c(length/no_of_videos):
        nxt = page + 1
    else:
        nxt = None
    context = {'videos': videos, 'prev': prev, 'nxt': nxt}
    return render(request, "content/videos.html", context)


def video_playing(request, slug):
    videoFound = Video.objects.filter(slug=slug).first()
    if videoFound:
        videoFound.views += 1
        videoFound.save()

    plvideos = 'None'
    if slug[3:11] != "xxxxxx00":
        plvideos = Video.objects.filter(slug__regex=f"^{slug[0:11]}.*")
    mvideos = list(Video.objects.all())
    more_videos = random.sample(mvideos, len(mvideos))
    context = {'name': videoFound, 'types': videoFound.source[0:5], 'plvideos': plvideos, 'mvideos': more_videos}
    return render(request, "content/video_playing.html", context)


def playlist(request):
    playlists = Playlist.objects.all()
    return render(request, "content/playlist.html", {'playlists': playlists})


def plvideos(request, slug):
    videos = Video.objects.filter(slug__regex=f"^{slug}.*")
    return render(request, "content/videos.html", {'videos': videos})
