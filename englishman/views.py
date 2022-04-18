from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import EnglishSerializer
from rest_framework.exceptions import APIException
import time
import spacy
nlp = spacy.load('en_core_web_sm')
from bs4 import BeautifulSoup
from collections import Counter

from .forms import CommonWordsForm

def five_noun(html_text, num=7):
    soup = BeautifulSoup(html_text, 'html.parser')
    text = str(soup.get_text().replace('\xa0', ''))
    doc = nlp(text)
    # all tokens that arent stop words or punctuations
    words = [(token.lemma_).lower()
            for token in doc
            if not token.is_stop and not token.is_punct]

    # noun tokens that arent stop words or punctuations
    # nouns = [(token.lemma_).lower()
    #         for token in doc
    #         if (not token.is_stop and
    #             not token.is_punct and
    #             token.pos_ == "NOUN")]

    # five most common tokens
    word_freq = Counter(words)
    common_words = word_freq.most_common(num)

    # # five most common noun tokens
    # noun_freq = Counter(nouns)
    # common_nouns = noun_freq.most_common(num)
    return common_words


class Success(APIException):
    status_code = status.HTTP_202_ACCEPTED
    default_detail = 'Success .'
    default_code = 'success'


class EnglishView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = EnglishSerializer



    def update(self, request, *args, **kwargs):
        text = request.data['text']
        start_time = time.time()
        k2 = five_noun(html_text=text, num=7)
        endtime = time.time() - start_time
        data = {'words': k2, 'time': endtime}
        raise Success(data)
    

    def get(self, request, *args, **kwargs):
        raise Success('a')

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


def common_words_view(request):
    if request.method == 'POST':
        form = CommonWordsForm(
            request.POST
        )
        if form.is_valid():
            cd = form.cleaned_data
            text = cd['text']
            num = cd['num']
            words = five_noun(text, num=num)
            return render(
                request,
                'englishman/index.html', {
                    'words': [word[0] for word in words]
                }
            )
    else:
        form = CommonWordsForm(request.POST)
    # print(text)
    return render(
        request,
        'englishman/index.html', {
            'form': form
        }
    )





def about(request):
    return render(
        request,
        'englishman/about.html', {
            
        }
    )


def api_doc(request):
    html = '<p>Some long string text You need summary for</p>'
    return render(
        request,
        'englishman/apidoc.html', {
            'html': html,
        }
    )