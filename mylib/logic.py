import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """Fetch wiki"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Search Wikipedia for names"""

    results = wikipedia.search(name)
    return results


def phrase(name):
    """Return phrases from wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
