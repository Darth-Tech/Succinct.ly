Feature: Preprocessing module 
    The following scenarios describe preprocessing module 
    that aids the scraper class in cleaning scraped data.

    Scenario: Removing links in the scraped page to avoid loss of potential information
    Given scraped data composed of html tags
    When I filter it out 
    Then I get filtered text of the type string devoid of html tags

    