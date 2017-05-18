# geolookup.py
Minimal latitude+longitude lookup:

```python
>>> import geolookup
>>> geolookup.lookup('29 Street No 7, Kigali, Rwanda')
(-1.923282, 30.128971)
```

Uses the free mapbox.com API (you need an access key). Off by a few kilometers for some unknown reason. 16 LoC for your pleasure, just copy-paste it into your project and BAM!
