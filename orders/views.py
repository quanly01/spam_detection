from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
import decimal
import pandas as pd 
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt
import seaborn as sns
from .models import Orders
from sklearn.feature_extraction.text import TfidfVectorizer


def mainpage(request):
    return render(request, 'orders/home.html')

def home(request):
    return render(request, 'orders/introduction.html')

def index(request):
    return render(request, "orders/index.html")

def analysis(request):
    return render(request, "orders/analysis.html")

@login_required
def love(request):
    return render(request, "orders/love.html")

@login_required
def sad(request):
    return render(request, "orders/sad.html")

@login_required
def predict(request):
    df= pd.read_csv("orders/spam.csv", encoding="latin-1")
    df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
	# Features and Labels
    df['label'] = df['v1'].map({'ham': 0, 'spam': 1})
    df['message']=df['v2']
    df.drop(['v1','v2'],axis=1,inplace=True)
    X = df['message']
    y = df['label']
    #Extract features
    cv = TfidfVectorizer(max_features=3000)
    X = cv.fit_transform(X) # Fit the Data
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    #Naive Bayes Classifier
    from sklearn.naive_bayes import MultinomialNB

    clf = MultinomialNB()
    clf.fit(X_train,y_train)
    clf.score(X_test,y_test)

    if request.method == 'GET':
        return HttpResponseRedirect(reverse('index'))


    if request.method == 'POST':
        message = request.POST['msg']
        # order = Orders(username = request.user.username, send_message = message)
        # order.save()
        data = [message]
        vect = cv.transform(data).toarray()
        prediction = clf.predict(vect)
        if prediction==0:
            order = Orders(username = request.user.username, send_message = message, status = 'Ham')
            order.save()
            return render(request, "orders/love.html")
        else:
            order = Orders(username = request.user.username, send_message = message, status = 'Spam')
            order.save()
            return render(request, "orders/sad.html")
    


