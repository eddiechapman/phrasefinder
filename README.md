# PhraseFinder

> A class for locating phrases in a text document.

## About

PhraseFinder is a technical exercise for the AbbVie NLP Ops position.

Written by Eddie Chapman, September 15th, 2022.


## Usage

Create an instance of the `PhraseFinder` class with document text and one or more search phrases.

```python
from phrasefinder import PhraseFinder

finder = PhraseFinder(text="Sample document text", "document", "text")

finder.search()  # [(7, 14), (16, 19)]
```

PhraseFinder returns an empty list if any of the phrases are missing from the text.

```python
finder = PhraseFinder(text="Sample document text", "text", "missing phrase")

finder.search()  # []
```

## Testing

Unit tests are located in `test.py`. Run the test suite with `python3 test.py`:

```commandline
$ python3 test.py

....
----------------------------------------------------------------------
Ran 4 tests in 0.002s
```