# text-geolocation-ail
Create a text geolocation module for AIL-FRAMEWORK

https://github.com/CIRCL/AIL-framework

![Image of AIL-framework](https://github.com/CIRCL/AIL-framework/blob/master/doc/logo/logo-small.png?raw=true)

This project try to use Mordecai

AIL Module Source Code :
[Text_geolocation.py](./bin/Text_geolocation.py)

## How text geolocation work 

Def : Geolocation is the task of identifying a location for a user or document.

Both language use and social ties are geographically biased, and thus can be used to recover the location of a user or a document via machine learning or neural networks.

The main idea is to learn the geographical distribution of a given word across different locations from training data, and use it to predict a location.

We can use the differences between different languages (English vs French) or even between countries which share the same languages (British=centre vs American English=center), but we can also use names of people, sports team, toponyms and dialectal terms.

We can also use adresses, local area (park, museum, ...), monuments, ... and resolve them to the correct place
