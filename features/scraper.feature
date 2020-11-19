Feature: Scraper feature functionalities
    Following scenarios describe the scraper class functionalities

    Scenario: Testing the basic parsing using BS4
    Given a web page url
    When we parse a page
    Then an object of "bs4.BeautifulSoup" is returned
