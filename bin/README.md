# Text Geolocation module

We use mordecai, a text geoparsing tool written in python 3.

Given a piece of text , it found their locations based on pre-trained models.

Extract the place names from a piece of text, resolve them to the correct place, and return their coordinates and structured geographic information.

### mordecai source code

https://github.com/openeventdata/mordecai

### How it work

Modekai return structured geographic information from unstructured text using model train via neural networks.

### Test

Pros:
- Seem easy to use and install.
- Ready to use model.

Cons:
- I can't get mordecai to work. I've used and install mordecai with pthon 2.7 and 3.4 and i got this error :
```python
/usr/lib/python3.4/importlib/_bootstrap.py:321: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  return f(*args, **kwds)
Using TensorFlow backend.
Traceback (most recent call last):
  File "Testmordecai.py", line 6, in <module>
    from mordecai import Geoparser
  File "/usr/local/lib/python3.4/dist-packages/mordecai/__init__.py", line 1, in <module>
    from .geoparse import Geoparser
  File "/usr/local/lib/python3.4/dist-packages/mordecai/geoparse.py", line 10, in <module>
    from . import utilities
  File "/usr/local/lib/python3.4/dist-packages/mordecai/utilities.py", line 180
    both_codes = {**nationality, **cts}
                   ^
SyntaxError: invalid syntax
```

### Source

Andrew Halterman, (2017). Mordecai: Full Text Geoparsing and Event Geocoding. Journal of Open Source Software, 2(9), 91, doi:10.21105/joss.00091:

https://github.com/openeventdata/mordecai/blob/master/paper/paper.md


