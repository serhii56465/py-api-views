from django.urls import path, include

from rest_framework import routers

from cinema.views import ActorList, ActorDetail, GenreList, \
    GenreDetail, CinemahallViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinemahall_list = CinemahallViewSet.as_view({"get": "list", "post": "create"})
cinemahall_detail = CinemahallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("cinemahalls/", cinemahall_list, name="cinemahall-list"),
    path("cinemahalls/<int:pk>/", cinemahall_detail, name="cinemahall-detail"),
    path("", include(router.urls))
]

app_name = "cinema"
