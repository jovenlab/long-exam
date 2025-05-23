
from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard URLs
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/chart-data/', views.dashboard_chart_data, name='dashboard_chart_data'),
    path('dashboard/category-data/', views.category_chart_data, name='category_chart_data'),
    
    # Transaction URLs
    path('transactions/', views.transactions, name='transactions'),
    path('transactions/create/', views.create_transaction, name='create_transaction'),
    path('transactions/edit/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    path('transactions/delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('export_csv/', views.export_transactions_csv, name='export_transactions_csv'),
    
    # Budget URLs
    path('budget/', views.set_budget, name='set_budget'),
    path('budget/edit/<int:budget_id>/', views.edit_budget, name='edit_budget'),
    path('budget/delete/<int:budget_id>/', views.delete_budget, name='delete_budget'),
]