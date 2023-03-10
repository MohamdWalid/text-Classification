# -*- coding: utf-8 -*-
"""Assignement2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11wD993t9YljjZ5uV1erBGyfhAQ57sR7k
"""

!pip install wikipedia
!pip install wikipedia-api

import wikipedia
import wikipediaapi
wiki_WIKI = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI )

"""#Domain(1)"""

import wikipediaapi
DOC1 = wiki_WIKI.page("Artificial Intelligence").text
DOC2 = wiki_WIKI.page("computer science").text
DOC3 = wiki_WIKI.page("Information Technology").text
DOC4 = wiki_WIKI.page("information systems").text

"""#Domain(2)"""

DOC5 = wiki_WIKI.page("cholera").text
DOC6 = wiki_WIKI.page("measles").text
DOC7 = wiki_WIKI.page("COVID-19").text
DOC8 = wiki_WIKI.page("Pneumonia").text

"""#Domain(3)"""

DOC9 = wiki_WIKI.page("BITCOIN").text
DOC10 = wiki_WIKI.page("Litecoin").text
DOC11 = wiki_WIKI.page("Dogecoin").text
DOC12 = wiki_WIKI.page("Ethereum").text

"""#Domain(4)"""

DOC13 = wiki_WIKI.page("Aspirin").text
DOC14 = wiki_WIKI.page("Paracetamol").text
DOC15 = wiki_WIKI.page("Insulin (medication)").text
DOC16 = wiki_WIKI.page("Minoxidil").text

"""#Domain(5)"""

DOC17 = wiki_WIKI.page("Microsoft Windows").text
DOC18 = wiki_WIKI.page("Linux").text
DOC19 = wiki_WIKI.page("macOS").text
DOC20 = wiki_WIKI.page("Android (operating system)").text

"""Topics"""

search = ["Artificial Intelligence","computer science","Information Technology","information systems",
          "cholera","measles","COVID-19","Pneumonia",
          "BITCOIN","Litecoin","Dogecoin","Ethereum",
          "Aspirin","Paracetamol","Insulin (medication)","Minoxidil",
          "Microsoft Windows","Linux","macOS","Android (operating system)"]
len(search)

"""Install nltk"""

!pip install nltk
import nltk
nltk.download('punkt')
nltk.download('stopwords')

"""Normalize The Words(Lower Case)

Remove Punkt

Tokenize The Documents

Remove Stop Words
"""

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))
def process(doc) :
  doc =doc.lower()
  doc= re.sub(r'[^\w\s]', ' ', doc)
  doc= nltk.word_tokenize(doc)
  doc = [w for w in doc if not w.lower() in stop_words]

  return doc

DOC1=process(DOC1)
DOC2=process(DOC2)
DOC3=process(DOC3)
DOC4=process(DOC4)
DOC5=process(DOC5)
DOC6=process(DOC6)
DOC7=process(DOC7)
DOC8=process(DOC8)
DOC9=process(DOC9)
DOC10=process(DOC10)
DOC11=process(DOC11)
DOC12=process(DOC12)
DOC13=process(DOC13)
DOC14=process(DOC14)
DOC15=process(DOC15)
DOC16=process(DOC16)
DOC17=process(DOC17)
DOC18=process(DOC18)
DOC19=process(DOC19)
DOC20=process(DOC20)

"""Store The Words Of Each Document"""

ALL_tokenized_sentences=[DOC1,DOC2,DOC3,DOC4,DOC5,DOC6,DOC7,DOC8,DOC9,DOC10,DOC11,DOC12,DOC13,DOC14,DOC15,DOC16,DOC17,DOC18,DOC19,DOC20]

import numpy as np
len(ALL_tokenized_sentences)
ALL_tokenized_sentences=np.array(ALL_tokenized_sentences)

"""Download The Drive in Google Colab"""

from google.colab import drive
import cv2
drive.mount('/content/drive/')

"""Download The Model in Google Colab"""

!sudo cp -v -r  "/content/drive/MyDrive/Google/GoogleNews-vectors-negative300.bin"  "/content/drive/MyDrive/model"

!gunzip "/content/drive/MyDrive/Google/GoogleNews-vectors-negative300.bin.gz"

import gensim
from gensim.models import Word2Vec , KeyedVectors
from gensim.models import Word2Vec
from gensim.models.wrappers import FastText
model = KeyedVectors.load_word2vec_format('/content/drive/MyDrive/Google/GoogleNews-vectors-negative300.bin', binary=True)

"""Word Embedding"""

d = []
Documents=[]
for i in range(0,len(ALL_tokenized_sentences)):
  for j in range(0,len(ALL_tokenized_sentences[i])):
    try:
      a=model[ALL_tokenized_sentences[i][j]]
      d.append(a)
    except:
      pass
  Documents.append(d.copy())
  d.clear()

len(Documents)

"""Document Embedding"""

sum = 0
average = 0
All_Documents = []
for i in range(0,len(Documents)):
  for j in range(0,len(Documents[i])):
    sum += Documents[i][j]
  average = sum / len(Documents[i])
  All_Documents.append(average)
  sum=0
  average=0

"""Test"""

def Test(sentence):
  z = []
  A = process(sentence)
  for i in range(0,len(A)):
     z.append(model[A[i]])

  sum = 0
  average = 0
  for i in range(0,len(z)):
     sum += z[i]
  average = sum / len(z)
  return average

def Distance(average):
   Similarity = []

   for i in range(0,len(All_Documents)):
     Similarity.append(np.sum(np.power(average-All_Documents[i],2)))

   Sort = 0
   for i in range(0,len(All_Documents)):
      Sort = np.argmin(Similarity)
      print(f'{search[Sort]} : {Similarity[Sort]}')
      Similarity[Sort] = 1000000000000
   print('----------------------------------------------------------')

sentence1 = Test('windows is operating system')
Distance(sentence1)

sentence2 = Test('Population density leads to the spread of diseases')
Distance(sentence2)

sentence3 = Test('There are many sections in the field of programming such as Computer Science')
Distance(sentence3)