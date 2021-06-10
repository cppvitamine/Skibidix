from backend.models import KindAnime,User, Kind, Anime,FavoritesKind,FavoritesAnime,Watching,UserRating

u = User(username="test", name="name", surname="smith")
u.save()

k = Kind(kind_name="shonen")
k.save()

k2= Kind(kind_name="isekai")
k2.save()

a = Anime(name="One Piece", global_rating = 5,plot="x", season = 1, last_episode=977, start_number_episode=1, last_update="2021-06-06", autodownlodable=True, finished=False)
a.save()

fk = FavoritesKind(fk_user=u, fk_kind=k)
fk.save()

fa = FavoritesAnime(fa_anime=a, fa_user=u)
fa.save()

w = Watching(w_user=u, w_anime=a, episode=1, seconds=134)
w.save()

ur = UserRating(ur_anime=a,ur_user=u,rating=4)
ur.save()

ka = KindAnime(ka_anime=a,ka_kind=k)
ka.save()

ki = Kind.objects.get(kind_name="shonen")
a = Anime(name="My Hero Academia",  global_rating = 1, plot="x", season=1, last_episode=13, start_number_episode=1, last_update="2016-06-26",autodownlodable=False, finished = True)
a.save()
a = Anime(name="My Hero Academia",  global_rating = 4, plot="x", season=2, last_episode=25, start_number_episode=0, last_update="2017-09-30",autodownlodable=False, finished = True)
a.save()
a = Anime(name="My Hero Academia",  global_rating = 3,plot="x", season=3, last_episode=25, start_number_episode=1, last_update="2018-09-29",autodownlodable=False, finished = True)
a.save()
a = Anime(name="My Hero Academia", plot="x", season=4, last_episode=25, start_number_episode=1, last_update="2020-04-04",autodownlodable=False, finished = True)
a.save()
a = Anime(name="My Hero Academia",  global_rating = 2,plot="x", season=5, last_episode=11, start_number_episode=1, last_update="2021-06-05",autodownlodable=False, finished = False)
a.save()
ka = KindAnime(ka_anime=Anime.objects.get(name="My Hero Academia", season=1),ka_kind=k)
ka.save()
ka = KindAnime(ka_anime=Anime.objects.get(name="My Hero Academia", season=2),ka_kind=k2)
ka.save()