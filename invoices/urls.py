from django.urls import path
from . import views


app_name = 'invoices'

urlpatterns = [
    path('', views.InvoiceListView.as_view(), name='main'),
    path('new/', views.InvoiceFormView.as_view(), name='create'),
    # path('<pk>/', views.SimpleTemplateView.as_view(), name='simple-template'),
    path('<pk>/', views.AddPositionsFormView.as_view(), name='detail'),
    path('<pk>/close/', views.CloseInvoiceView.as_view(), name='close'),
    path('<pk>/update/', views.InvoiceUpdateView.as_view(), name='update'),
    path('<pk>/pdf/', views.invoice_pdf_view, name="pdf"),
    path('<pk>/delete/<int:position_pk>/', views.InvoicePositionDeleteView.as_view(), name='position-delete'),
]