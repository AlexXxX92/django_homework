from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

# CONTENT =
def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    import csv
    content = []
    with open('data-398-2018-08-30.csv', newline='', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            content.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(content, 10)
    # print(content)
    page = paginator.get_page(page_number)
    # print(page.object_list[0])


    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
