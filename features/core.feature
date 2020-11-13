Feature: Core summariser and its models
    The following scenarios encapsulate the functionalities
    Of the core summarizing component of the application

    
    Scenario: Summarizer default features
    Given a normal text to summarise with default settings
    When we summarize without parameters
    """
    The Chrysler Building, the famous art deco New York skyscraper, will be sold for a small fraction of its previous sales price.
    """
    Then a string is returned

    