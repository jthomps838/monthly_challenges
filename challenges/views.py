from django.http.response import HttpResponseNotAllowed, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

months = {
    'january': 0,
    'february': 1,
    'march': 2,
    'april': 3,
    'may': 4,
    'june': 5,
    'july': 6,
    'august': 7,
    'september': 8,
    'october': 9,
    'november': 10,
    'december': 11
}

challenge_goals = [
    'January: Do 50 push-ups a day',
    'February: Run a 5k a week',
    'March: Join a book club',
    'April: Do 100 sit-ups a day',
    'May: Run a 10k every two weeks',
    'June: Do 50 jumping jacks a day',
    'July: Swim at least 10 miles',
    'August: Eat Healthy',
    'September: Watch football every weekend',
    'October: Go to the moutains for a hike',
    'November: Enjoy family for Thanksgiving',
    'December: Enjoy Christmas with family'
]


def challenges(request):
    return HttpResponse('Check out all of our challenges')


def monthly_challenge(request, month):
    if month in months:
        month_index = months[month]
        return HttpResponse(f'Challenge for {challenge_goals[month_index]}')
    return HttpResponseNotFound('No page found')
