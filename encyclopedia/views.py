from django.shortcuts import render
from . import util
import random
import markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def get(request, title):
    m = util.gett(title)
    h = util.convert_markdown_to_html(m)

    return render(request, "encyclopedia/entry_search.html", {
        "title": title,  # Pass the 'title' variable
        "markdown": m,  # Pass the 'h' variable
    })
def create(request):
    return render(request, "encyclopedia/create.html", {
        "entries": util.list_entries()
    })
    
def search_results(request):
    text="Veuillez réessayer ultérieurement , ce title est non valide ."
    query = request.GET.get('query')
    if util.gett(query):
        m= util.gett(query)
        h = util.convert_markdown_to_html(m)
        return render(request, 'encyclopedia/search_results.html', {'query': h})
    else:
        if query=="":
            text="Veuillez réessayer ultérieurement , ce title est non valide ."
            return render(request, 'encyclopedia/search_results.html', {'query': (text) })
        else:
            l=util.list_entries()
            lr=[]
            i=0
            while i<=len(l)-1:
                if query==l[i][1:]:
                     lr.append(l[i])
                i+=1 
            if lr:
                return render(request, 'encyclopedia/search2_results.html', {'query': (lr) })
            else:
                return render(request, 'encyclopedia/search3_results.html', {'query': (text) })
            
def createpage(request):
    title = request.GET.get('title')
    markdown = request.GET.get('markdown')
    if util.gett(title):
        text="Ce titre est deja existe Veuillez réessayer un autre SVP ."
        return render(request, 'encyclopedia/create.html', {'title': (text) })
    else:
        util.save_entry(title,markdown)
        return render(request, 'encyclopedia/createpage.html', {'title': title, 'markdown': markdown})

def randomm(request):
    l = util.list_entries()
    i = random.randint(0, len(l) - 1)  
    title=l[i]
    m= util.gett(title)
    h = util.convert_markdown_to_html(m)
    return render(request, 'encyclopedia/random.html', {'query':h}) 

def edit(request,title):
    m= util.gett(title)
    return render(request, 'encyclopedia/edit.html', {'title': title, 'markdown': m })

def save(request):
    title = request.GET.get('title')
    markdown = request.GET.get('markdown')
    util.save_entry(title,markdown)
    return render(request, 'encyclopedia/save.html', {'title': title, 'markdown': markdown})


    





    
