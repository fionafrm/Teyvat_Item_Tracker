from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Sweet Madame',
        'desc': 'Depending on the quality, Sweet Madame restores 20/22/24% of Max HP and an additional 900/1,200/1,500 HP to the target character. Like most foods, this cannot target other players' + ' characters in Co-Op Mode. When Rosaria cooks Sweet Madame, there is a chance that Dinner of Judgment will be created instead.',
        'amt' : '150',
        'category' : 'food'
    }

    return render(request, "main.html", context)