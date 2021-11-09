from django.shortcuts import render
from autocorrect import Speller
from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import regexp_tokenize

from django.core.files.storage import default_storage


# Create your views here.

# Password - qwerty54321

def index(request):
    return render(request, 'index.html')

def word_check(request):
    if(request.method == "GET"):
        #Get the word

        # elemnatal
        word = request.GET.get('inputWord')
        spell = Speller()
        corrected_word = spell(str(word).split(' ')[0])
        # print(spell(str(word)),"SARTHAK")
        context = {
                'word': word,
                'corrected_word': corrected_word,
            }
        return render(request, 'word_check.html', context)
    return render(request, 'word_check.html')

def sentence_check(request):
    if(request.method == "GET"):
        #Get the sentence

        # How you douing thees dyas?
        # How yuo doing thees dyas?
        sentence = request.GET.get('inputSentence')
        spell = Speller()
        text = str(sentence)
        corrected_sentence = spell(text)
        tokenized = []
        tokenized = word_tokenize(text)
        word_tokenize_corrected_sentence = ""
        # print(tokenized)
        for i in tokenized:
            word_tokenize_corrected_sentence+=spell(i)+" "


        tokenizer = TreebankWordTokenizer()
        tokenized = tokenizer.tokenize(text)
        TreebankWordTokenizer_corrected_sentence = ""
        # print(tokenized)
        for i in tokenized:
            TreebankWordTokenizer_corrected_sentence+=spell(i)+" "

        
        tokenizer = WordPunctTokenizer()
        tokenized = tokenizer.tokenize(text)
        # print(tokenized)
        WordPunctTokenizer_corrected_sentence = ""
        for i in tokenized:
            WordPunctTokenizer_corrected_sentence+=spell(i)+" "

        
        tokenizer = RegexpTokenizer("[\w']+")
        tokenized = tokenizer.tokenize(text)
        RegexpTokenizer_corrected_sentence = ""
        # print(tokenized)
        for i in tokenized:
            RegexpTokenizer_corrected_sentence+=spell(i)+" "

        
        tokenized = regexp_tokenize(text, "[\w']+")
        regexp_tokenize_corrected_sentence = ""
        # print(tokenized)
        for i in tokenized:
            regexp_tokenize_corrected_sentence+=spell(i)+" "

        
        # print(type(sentence),"SARTHAK")
        context = {
                'sentence': sentence,
                'corrected_sentence': corrected_sentence,
                'word_tokenize_corrected_sentence': word_tokenize_corrected_sentence,
                'TreebankWordTokenizer_corrected_sentence': TreebankWordTokenizer_corrected_sentence,
                'WordPunctTokenizer_corrected_sentence': WordPunctTokenizer_corrected_sentence,
                'RegexpTokenizer_corrected_sentence': RegexpTokenizer_corrected_sentence,
                'regexp_tokenize_corrected_sentence': regexp_tokenize_corrected_sentence,
            }
        return render(request, 'sentence_check.html', context)
    return render(request, 'sentence_check.html')

def document_check(request):
    if(request.method == "POST"):
        #Get the document
        document = request.FILES['inputFile']
        print(document)
        if default_storage.exists('static/file.txt'):
            default_storage.delete('static/file.txt')
        if document!='':
            path = default_storage.save('static/file.txt', document)

            document = ""
            corrected_document = ""
            with open('static/file.txt') as f:
                contents = f.readlines()
                spell = Speller()
                for content in contents:
                    document += str(content)
                    corrected_document += spell(str(content))
                    # print(document,"SARTHAK")
        context = {
                'document': document,
                'corrected_document': corrected_document,
            }
        return render(request, 'document_check.html', context)
    return render(request, 'document_check.html')

def website_info(request):
    return render(request, 'website_info.html')

def about(request):
    return render(request, 'about.html')

def reference(request):
    return render(request, 'reference.html')