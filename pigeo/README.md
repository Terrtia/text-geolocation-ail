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

pigeo mode: 
- Shell mode:
  - Take an input text and geolocate it.
  - Activate shell mode : *python pigeo.py --mode shell*
  - Return the results in JSON format.
  - Example of execution:
  ![Image of pigeo, shell mode,exemple of execution](https://github.com/Terrtia/text-geolocation-ail/blob/master/pigeo/pigeo-test_shell_mode.png)
- Web mode:
  - pigeo also get a web interface to copy/paste text and display result.
  - Activate Web mode : *python pigeo.py --mode web*
  - Example of execution:
  ![Image of pigeo, web mode,exemple of execution](https://github.com/Terrtia/text-geolocation-ail/blob/master/pigeo/pigeo_web_mode_test.png)
- Library mode:
  - pigeo can be use as a librairy when many documents are needed to be geolocated.
  - Code example:
```python
import pigeo

# load the world model (default)
pigeo.load_model()

# geolocate a sentence
pigeo.geo("gamble casino city")

# geolocate a Twitter user
pigeo.geo(’@POTUS’)

# geolocate a list of texts
pigeo.geo([’city centre’, ’city center’])
```
- Twitter user geolocation:
  - pigeo takes the user name of a Tweeter user and geolocate him.
  - Can be done in any of Shell, Web or Library modes.
  - Require an internet connection and valid Twitter authentication information (set in *twitterapi.py*).
- Training a new model:
  - Train a new model in librairy mode using list of text samples and a list of corresponding coordinates as a (latitude, longitude) tuple.
  - Code example:
```python
import pigeo

# train a model and save it in ’example’
pigeo.train_model([’text1’, ’text2’], [(lat1, lon1), (lat2, lon2)], num_classes=2, model_dir=’example’)

# load and use the new model
pigeo.load_model(model_dir=’example’)
```
- Network-based model:
  - Given a Twitter user, the timeline is downloaded and the @-mentions are matched with the hashed user account names. The median location of the matched users is returned as the prediction.
  - Code example:
```python
import pigeo

# load lpworld
pigeo.load_lpworld()

# geolocate a Twitter user
pigeo.geo_lp(’@potus’)
```

Pros:
- Easy to use and install.
- Ready to use model.
- can train models.

Cons:
- There is some accuracy problems because the data is more than 5 years old.
- Don't recognize addresses (test with US and FR).


### Source

pigeo, A Python Geotagging Tool (Afshin Rahimi, Trevor Cohn, and Timothy Baldwin):

https://github.com/Terrtia/text-geolocation-ail/blob/master/pigeo/pigeo_a_python_geotagging_tool.pdf


