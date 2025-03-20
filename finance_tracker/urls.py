from django.urls import path

from . import views

urlpatterns = [  
    # -----------------------------<< Authentication >>--------------------------
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('reset_password/',views.reset_password_view,name='reset_password'),

    #-----------------------------<< User Profile >>--------------------------
    path('', views.dashboard, name='dashboard'),
    path('finance/', views.finance, name='finance'),
    path('statements_form/', views.statements, name='statements_form'),
    path('statement/<int:month>/<int:year>/', views.generate_statement, name='generate_statement'),

    #----------------------------<< Download CSV, PDF, Excel >>---------------------------
    path('finance/download_statement/<int:month>/<int:year>/', views.generate_statement, name='download_statement'),
    path('finance/download_statement/<int:month>/<int:year>/', views.download_statement_pdf, name='download_statement_pdf'),
    path('finance/download_statement_excel/<int:month>/<int:year>/', views.generate_statement, name='download_statement_excel'),
   
    #----------------------------<< Add, Update, Delete >>---------------------------
    path('add_income/', views.add_income, name='add_income'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('add_savings/', views.add_savings, name='add_savings'),  
    path('update_income/<int:id>/', views.update_income, name='update_income'),
    path('update_expense/<int:id>/', views.update_expense, name='update_expense'),
    path('update_savings/<int:id>/', views.update_savings, name='update_savings'),
    path('delete_savings/<int:pk>/', views.delete_savings, name='delete_savings'),
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),
    path('delete_income/<int:pk>/', views.delete_income, name='delete_income'),
]
