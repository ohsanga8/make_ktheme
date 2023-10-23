from django.shortcuts import render
from make_ktheme.models import Ktheme


# Create your views here.
def main(request):
    user = request.user
    user_kthemes = Ktheme.objects.filter(user=user)
    return render(request, "main/main.html", {"user_kthemes": user_kthemes})
