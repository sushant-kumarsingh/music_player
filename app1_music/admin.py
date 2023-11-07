from django.contrib import admin

# Register your models here.

from .models import Artist,Album,song

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display=("id", "artistName","created","last_updated")

@admin.register(song)
class songAdmin(admin.ModelAdmin):
    list_display=("id","album","song","songName","songThumbnail","created","last_updated")


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display=("artist","albumName","created","last_updated")