from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def count(request):
  fulltext = request.GET['full1text']
  wordlist = fulltext.split()
  worddictionary = {}
  for word in wordlist:
    if word in worddictionary:
      #Increase
      worddictionary[word] += 1
    else:
      worddictionary[word] = 1
  return render(request, 'main/count.html', {'fulltext': fulltext, 'kcount': len(wordlist), 'worddictionary':worddictionary.items})