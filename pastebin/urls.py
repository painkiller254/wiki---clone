from django.urls import path
from .views import PasteCreate, PasteDetail, PasteList, PasteDelete, PasteUpdate

urlpatterns = [
    path(r'', PasteCreate.as_view(), name='create'),
    path('paste/<int:pk>', PasteDetail.as_view(), name='pastebin_paste_detail'),
    path('paste/<int:pk>', PasteList.as_view(), name='pastebin_paste_list'),
    path('paste/delete/<int:pk>', PasteDelete.as_view(), name='pastebin_paste_delete'),
    path('paste/edit/<int:pk>', PasteUpdate.as_view(), name='pastebin_paste_edit'),
    
]
