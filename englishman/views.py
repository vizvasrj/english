
# Create your views here.
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

def five_noun(html_text, num=7):
    soup = BeautifulSoup(html_text, 'html.parser')
    text = str(soup.get_text())
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
