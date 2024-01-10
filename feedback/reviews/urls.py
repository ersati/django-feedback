from django.urls import path

from . import views
urlpatterns = [
    # functional paths:
    # path("", views.review),
    # path("thank-you", views.thank_you)
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankyouView.as_view()),
    path("reviews", views.ReviewListView.as_view()),
    path("reviews/<int:id>", views.ReviewListView.as_view()),
    
]
