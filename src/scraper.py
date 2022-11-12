import requests as _request
import bs4 as _bs4


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


# create url function
url = _create_url("knowledge")
# create soup function
soup = _get_page(url)

# store all quotes in a variable called "raw_quotes"
raw_quotes = soup.find_all(class_="quoteText")

# write a for loop to loop through all of the quotes
for quote in raw_quotes:
    print(quote.contents)
