from django.shortcuts import render

import csv

def inflation_view(request):
    template_name = 'inflation.html'

    rows = []
    with open('inflation_russia.csv', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            counter = 0
            while counter != len(row):
                if counter >= 1:
                    try:
                        row[counter] = float(row[counter])
                    except ValueError:
                        pass
                counter += 1
            rows.append(row)

    context = {'rows': rows}

    return render(request, template_name,
                  context)