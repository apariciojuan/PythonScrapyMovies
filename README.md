# Python Scrapy Movies

Scrapy with Python
That script pull data about movies and diferente links where is possible watch them.
I use Selenium only for activate some links make in Javascript, hidden in the began.
You can see data in a console, in json with ran command under or you can use code commented on pipelines.py for save data en MongoDB.

Requerimient: Python 3.5.2, Scrapy 1.5, Selenium 3.14.0

Generate Json with data.
Run: scrapy crawl movie -o items.json

