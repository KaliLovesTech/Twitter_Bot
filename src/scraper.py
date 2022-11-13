import requests as _request
import bs4 as _bs4
import constants as _constants


# define function to format the url
def _create_url(tag: str) -> str:
    return f"https://www.goodreads.com/quotes/tag/{tag}"


# define function to get page and make it an object
def _get_page(url: str) -> _bs4.BeautifulSoup:
    # request the url using the "get" method
    page = _request.get(url)
    # create the BeautifulSoup object
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    # return the BeautifulSoup object
    return soup


# define a function to extract the author and and quote
def _extract_author_and_quote(quote):
    # get first quote
    quote_text = quote.contents[0].strip()
    # get author
    author = quote.find(class_="authorOrTitle").text.strip()

    # return tuple
    return quote_text, author


# define a function that will loop through all of the quotes
def scrape_quotes():
    # create a list that will contain all of the quotes, authors, genre
    collections = list()
    # for loop to loop through all of the tags
    for tag in _constants.TAGS:
        # get url and pass in the tag name
        url = _create_url(tag)
        # create the soup object and pass in the url
        soup = _get_page(url)
        # use 'find_all' method and store all quotes in a variable called "raw_quotes"
        raw_quotes = soup.find_all(class_="quoteText")
        # loop through all of the quotes
        for quote in raw_quotes:
            quote_text, author = _extract_author_and_quote(quote)
            # define the dictionary for the collections list
            data = {
                "quote": quote_text,
                "author": author,
                "genre": tag,
            }
            # append data to collections list
            collections.append(data)

    return collections


print(scrape_quotes())
