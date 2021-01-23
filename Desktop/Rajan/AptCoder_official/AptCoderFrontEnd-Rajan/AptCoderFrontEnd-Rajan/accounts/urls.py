from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('coupon_code_verify/<int:pk>/', views.coupon_code_verify, name='coupon_code_verify'),
	path('registered_course/', views.registered_courselist, name='register_course'),
	path('information_details/', views.information_details, name='information_details'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
	path('reset_password/',
		auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
		name = "reset_password"),

	path('reset_password_sent/',
		auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
		name = "password_reset_done"),

	path('reset/<uidb64>/<token>/',
		auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
		name = "password_reset_confirm"),
	path('reset_password_complete/',
		auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
		name = "password_reset_complete"),
	path('oneClickRegistration/', views.oneClickRegistration, name='oneClickRegistration')
		]
