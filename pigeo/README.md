# PIGEO

pigeo is a document or Twitter user geolocation tool written in python 2.7.

Given a piece of text or a Twitter user, it can predict their locations based on pre-trained models.

### pigeo source code

https://github.com/afshinrahimi/pigeo

### How it work

The source for the model are focused on Twitter data, tweets and geotagged users.
the dataset text are predominantly in english, but also include a rich variety of other languages.

pigeo use machine learning to recover the location of a user or a document.

### Test


- And if you have sub points, put two spaces before the dash or star:
  - Like this
  - And this

pigeo mode: 
- Shell mode:
  - Take an input text and geolocate it.
  - Activate shell mode : *python pigeo.py --mode shell*
  - Return the results in JSON format.
  - Example of execution:
  ![Image of pigeo, shell mode,exemple of execution](https://github.com/Terrtia/text-geolocation-ail/blob/master/pigeo/pigeo-test_shell_mode.png)
- Web mode
- Library mode
- Twitter user geolocation
- Training a new model
- Network-based model

pros:
- easy to use and install
- ready to use model
cons:
- there is some accuracy problems because the data is more than 5 years old
- don't recognize addresses (test with US and FR)


### Source

pigeo, A Python Geotagging Tool (Afshin Rahimi, Trevor Cohn, and Timothy Baldwin):

https://github.com/Terrtia/text-geolocation-ail/blob/master/pigeo/pigeo_a_python_geotagging_tool.pdf


