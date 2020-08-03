from django.urls import path
from django.contrib.auth.decorators import login_required

from linktosite.views import NewLinkView, \
    NewCategoryView, \
    MainView, \
    EditLinkView, \
    delete_link, \
    delete_cat, \
    UpdateLinkView, \
    RenameCatView

urlpatterns = [
    path('new_link/', login_required(NewLinkView.as_view()), name='new_link_view'),
    path('new_category/', login_required(NewCategoryView.as_view()),
         name='new_category_view'),
    path('edit/<int:id>/', login_required(EditLinkView.as_view()),
         name='edit_link_view'),
    path('delete_link/<int:id>/', delete_link, name='delete_link'),
    path('update/<int:id>/', login_required(UpdateLinkView.as_view()),
         name='update_link_view'),
    path('delete_cat/<int:id>/', delete_cat,
         name='delete_cat'),
    path('rename_cat/<int:id>/',
         login_required(RenameCatView.as_view()), name='rename_cat_view'),
    path('', MainView.as_view(), name='main_view'),
]
