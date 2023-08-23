# ## Amabel Nabila
# In[1]:


get_ipython().system('pip install scrapy')


# In[2]:


import scrapy

class LinkListsSpider(scrapy.Spider):
    name = "link_lists"
    start_urls = [
        'https://en.wikipedia.org/wiki/Lists_of_musicians'
    ]

    def parse(self, response):
        genre_links = response.css('div#mw-content-text div.mw-parser-output div.div-col.columns.column-width ul li a::attr(href)').getall()
        genre_links = [link for link in genre_links if link.startswith('/wiki/List_of')]
        for link in genre_links:
            yield response.follow(link, self.parse_links)

    def parse_links(self, response):
        artist_links = response.css('div.div-col.columns.column-width ul li a[href^="/wiki/"]::attr(href)').getall()
        for link in artist_links:
            yield {
                'link': 'https://en.wikipedia.org' + link
            }  

