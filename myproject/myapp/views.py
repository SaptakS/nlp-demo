# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import *

import os
import algorithms.pronoun.hobbs.hobbsCalc as hp


def home(request):    
    ''' Renders the template for home page of the website '''
    return render(request, 'home.html')

def hobbs(request):
    
    if request.method == 'POST':
        form = HobbsForm(request.POST, request.FILES)
        if form.is_valid():
            #text = request.POST.get('text')
            pronoun = request.POST.get('pronoun')
            doc_name = request.FILES['docfile']
            print doc_name
            newdoc = Document(docfile = doc_name)
            url1 = os.path.join('/media/documents/', str(doc_name))        
            url = os.path.realpath(os.path.join(os.path.realpath(os.path.dirname(__file__)), '../media/documents/', str(doc_name)))            
            if url1 in [document.docfile.url for document in Document.objects.all()]:
                os.remove(url)
            newdoc.save() 
            argv = [""]
            argv.append(url)
            argv.append(pronoun)
            print argv
            tree,noun = hp.calc(argv)
            print "Tree: ", tree
            print "Noun: ", noun
            request.session["tree"] = tree
            request.session["noun"] = noun
            request.session["pronoun"] = pronoun

            return HttpResponseRedirect(reverse('myproject.myapp.views.hobbs'))
    else:
        form = HobbsForm() # A empty, unbound form

    if "tree" in request.session.keys():
        return render_to_response(
            'hobbs.html',
            {'form':form, 'tree': request.session.pop('tree', None), 'noun':request.session.pop('noun', None), 'pronoun':request.session.pop('pronoun', None)},
            context_instance=RequestContext(request)
        )
    else:    
        return render_to_response(
            'hobbs.html',
            {'form':form},
            context_instance=RequestContext(request)
        )
