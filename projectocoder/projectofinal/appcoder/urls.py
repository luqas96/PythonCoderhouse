from django.contrib import admin
from django.urls import path

from .views import (
    cursos_view,
    inicio_view,
    cursos_crud_read_view,
    profesor_view,
    profesores_crud_read_view,
    profesores_crud_delete_view,
    profesores_crud_update_view,
    # CBV
    CursoCreateView,
    CursoDetail,
    CursoDeleteView,
    CursoListView,
    CursoUpdateView
)

urlpatterns = [
    path("inicio/", inicio_view),
    path("cursos/", cursos_view),
    path("cursos-lista/", cursos_crud_read_view),
    path("profesores/", profesor_view),
    path("profesores-lista/", profesores_crud_read_view),
    path("profesores-eliminar/<profesor_email>/", profesores_crud_delete_view),
    path("profesores-editar/<profesor_email>/", profesores_crud_update_view),

    ### CBV

    path("curso/list", CursoListView.as_view(), name="curso-list"),
    path("curso/new", CursoCreateView.as_view(), name="curso-create"),
    path("curso/<pk>", CursoDetail.as_view(), name="curso-detail"),
    path("curso/<pk>/update", CursoUpdateView.as_view(), name="curso-update"),
    path("curso/<pk>/delete", CursoDeleteView.as_view(), name="curso-delete"),

]