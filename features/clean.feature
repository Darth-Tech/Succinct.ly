Feature: Preprocessing module # features/preproc.feature:1
  The following scenarios describe preprocessing module
  that aids the scraper class in cleaning scraped data.

  Scenario: Removing links in the text to summarize
  Given a text with hyperlinks
  """
  This is an excellent example of the sort of book to http://testsite.org engage with the strongest versions of. then sketches in the context that pacifists often leave out.
  It turns out the body https://theanarchistlibrary.org/ text only accounts for Diction Quibble: Though the text is largely reada
  """
  When we preprocess this 
  Then the result splits the text and the hyperlinks to summarise