# Sentiment-Analysis-on-Amazon-Product-Reviews-DA2
The objective of this paper is to classify the positive and negative reviews of the customers over different products and build a supervised learning model to polarize large amounts of reviews.

## Task Assigned by Technocolabs 
![Technocolabs](https://i.postimg.cc/Ls0bsz61/logo1.png)

## Check the working of the application here

<a href="https://amaz-reviews.herokuapp.com/">Click here</a>

## Dataset used 

1429_1.csv<br>
Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv<br>
Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv
## Technologies used

Python
Jupyter notebook- For editing and saving the python files.<br>
Heroku- To deploy models on heroku cloud.<br>
Tableau- To create vizualisation.<br>

## Libraries Used:

Regex(re)- To remove punctuation from the text.<br>
ntlk- To shorten the words.<br>
Sklearn- For Support Vector Machine (SVM) model, splitting the data into training and testing dataset, creating classification report, confusion matrix, fine tuning the models and tokenizing each word in reviews using CountVectorizer.<br>
Pickle- To deploy model into .pkl file for further processing in flask app.<br>
Flask- To create a web app for GUI application.<br>
