from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.
#functional approach
# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # create a model from form that isnt connect with the model.
#             # review = Review(
#             #     user_name= form.cleaned_data['user_name'], 
#             #     review_text = form.cleaned_data['review_text'], 
#             #     raiting = form.cleaned_data['raiting'])
#             # review.save()
#             form.save()
#             print(form.cleaned_data)
#             return HttpResponseRedirect("/thank-you")
#     else:        
#         form = ReviewForm()
#     return render(request, "reviews/review.html", {
#         "form": form
#     })
# def thank_you(request):
#     return render(request, "reviews/thank_you.html")
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
         "form": form
     })
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html", {
         "form": form
     })

class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "this is a great" 
        return context
    

class ReviewListView(TemplateView):
    template_name = "reviews/review_list.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context
    

class SingleReviewView(TemplateView):
    template_name = "reviews/single_review.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        review_id = kwargs.get("id")
        reviews = Review.objects.get(pk=review_id)
        context["reviews"] = reviews
        return context