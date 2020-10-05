# Text summarizer as a Chrome extension
![Logo](logo.png)
This repository contains the source code for the chrome extension to automatically summarize text in a given page.

It uses the [Bert Extractive Summarizer](https://pypi.org/project/bert-extractive-summarizer/) by Derek Miller.
```
pip install bert-extractive-summarizer
```

## To run the production server locally-
```
docker-compose -f docker-compose.prod.yml up
```
## To run the development server-
```
docker-compose -f docker-compose.yml up
```

Please note that you must have Nginx configured in your system for this to work. 

