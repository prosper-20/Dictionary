from django.shortcuts import render
import bs4
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):

    word = request.GET['word']

    res = requests.get('https://www.dictionary.com/browse/'+word)
    res2 = requests.get('https://www.thesaurus.com/browse/'+word)
    

    if res:
        soup = bs4.BeautifulSoup(res.text, 'lxml')

        meaning = soup.find_all('div', {'value': '1'})
        meaning1 = meaning[0].getText()
    else:
        word = 'Sorry, '+ word + ' Is Not Found In Our Database'
        meaning = ''
        meaning1 = ''

    if res2:
        soup2 = bs4.BeautifulSoup(res2.text, 'lxml')

        synonyms = soup2.find_all('a', {'class': 'css-1kg1yv8 eh475bn0'})
        ss = []
        for b in synonyms[0:]:
            re = b.text.strip()
            ss.append(re)
        se = ss
        new = " ".join(se)
        

        

        antonyms = soup2.find_all('a', {'class': 'css-15bafsg eh475bn0'})
        aa = []
        for c in antonyms[0:]:
            r = c.text.strip()
            aa.append(r)
        ae = aa
        newest = " ".join(ae)
    else:
        se = ''
        ae = ''


    results = {
        'word' : word,
        'meaning' : meaning1,
    }

    # You changed it to word_2.html from word.htm
    return render(request, 'word_2.html', {'se': se, 'ae': ae, 'new':new, 'newest': newest, 'results': results})




def HomeView(request):
    return render(request, 'mydictionary/index.html')


def SearchView(request):
    word = request.GET['word']

    response = requests.get('https://www.dictionary.com/browse/'+word)
    response2 = requests.get('https://www.thesaurus.com/browse/'+word)

    if response:
        soup_1 = bs4.BeautifulSoup(response.text, 'lxml')

        meaning = soup_1.find_all('div', {'value': '1'})
        meaning_1 = meaning[0].getText()
    else:
        word = f"Sorry we couldn't find your word {word} in our records."
        meaning = ''
        meaning_1 = ''

    if response2:
        soup_2 = bs4.BeautifulSoup(response2.text, 'lxml')

        synonyms = soup_2.find_all('a', {'class': 'css-r5sw71-ItemAnchor etbu2a31'})
        synonym_list = []
        for b in synonyms[0:]:
            re = b.text.strip()
            synonym_list.append(re)
        main_synonym_list = synonym_list

        antonyms = soup_2.find_all('a', {'class': 'css-lqr09m-ItemAnchor etbu2a31'})
        antonyms_list = []
        for c in antonyms[0:]:
            r = c.text.strip()
            antonyms_list.append(r)
        main_antonym_list = antonyms_list
    else:
        main_synonym_list = ''
        main_antonym_list = ''


    results = {
        'word' : word,
        'meaning' : meaning_1,
    }

    return render(request, 'mydictionary/serach.html', {'main_synonym_list': main_synonym_list, 'main_antonym_list': main_antonym_list, 'results': results})


def word(request):
    
    word = request.GET['word']

    res = requests.get('https://www.dictionary.com/browse/'+word)
    res2 = requests.get('https://www.thesaurus.com/browse/'+word)
    

    if res:
        soup = bs4.BeautifulSoup(res.text, 'lxml')

        meaning = soup.find_all('div', {'value': '1'})
        meaning1 = meaning[0].getText()
    else:
        word = 'Sorry, '+ word + ' Is Not Found In Our Database'
        meaning = ''
        meaning1 = ''

    if res2:
        soup2 = bs4.BeautifulSoup(res2.text, 'lxml')

        synonyms = soup2.find_all('a', {'class': 'css-r5sw71-ItemAnchor etbu2a31'})
        ss = []
        for b in synonyms[0:]:
            re = b.text.strip()
            ss.append(re)
        se = ss
        

        

        antonyms = soup2.find_all('a', {'class': 'css-lqr09m-ItemAnchor etbu2a31'})
        aa = []
        for c in antonyms[0:]:
            r = c.text.strip()
            aa.append(r)
        ae = aa
    else:
        se = ''
        ae = ''


    results = {
        'word' : word,
        'meaning' : meaning1,
    }


    return render(request, 'word.htm', {'se': se, 'ae': ae, 'results': results})





























