from django.shortcuts import render

def main(request):
    return render(request, 'shop_app/index.html')
