from sys import argv
from bs4 import BeautifulSoup

def getSoupObject(url):
    """Will return the soup object for our url"""

    try:

        # getting the site we want to scrape in a "response object", will timeout if connection takes more then 10 seconds or data hasn't been send for more then 10 seconds
        response = requests.get(url, timeout=10)
        source = response.content

        # calling raise_for_status to see if any HTTP errors occured.
        response.raise_for_status()

    # catching http errors (like 401 Unauthorized)
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error: ", errh)
        return None
    # catching connection errors
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting: ", errc)
        return None
    # catching timeout errors
    except requests.exceptions.Timeout as errt:
        print("Timeout Error: ", errt)
        return None
    # catching other exceptions (more general ones)
    except requests.exceptions.RequestException as err:
        print("General Error: ", err)
        return None

    # When no errors have occured
    else:

        # parsing the source code in to a soup object using a lxml parser
        soup = BeautifulSoup(source, "lxml")

        # returning our soup object
        return soup

def scrapeAstroidNames(amountOfNamesNeeded):
    """Will scrape x amount of astroid names"""

    astroidNames = []
    url = "https://space.fandom.com/wiki/List_of_named_asteroids_(A-E)"
    soup = getSoupObject(firstPageURL)

    # Finding 200 astroid names
    items = soup.find_all("a", {"rel":"nofollow"}, limit=200)

    # Looping thru item and getting the text
    for item in items:

        astroidName = item.text
        
        # if the name contains page does not exist
        if (astroidName.count("(page does not exist)") > 0):

            astroidName = astroidName.replace("(page does not exist)", "")

        # adding the astroid name to the array
        astroidNames.append(astroidName)

    return astroidNames
