# Webscrapping: recycle the web

This is a joint project of @ryanprior and @ckshobha created at Madison Python's inaugural Pair Programming Night.

It downloads headlines from CNN, replacing the words with synonyms to create familiar-sounding phrases that are often surreal and nonsensical.

### Dependencies

* Python 3
* pypy packages:
  * [`beautifulsoup4`](https://pypi.python.org/pypi/beautifulsoup4)
  * [`py_thesaurus`](https://pypi.python.org/pypi/py-thesaurus)
* Internet connection

### Running

With locally installed dependencies:

```shell
python start.py
```

Or in a Docker container:

```shell
docker build --tag webscrapping .
docker run --rm -v ${PWD}:/py webscrapping python /py/start.py
```