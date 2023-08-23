# ## Amabel Nabila


# In[1]:


import scrapy

class LinksSpider(scrapy.Spider):
    name = "links"
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_African-American_musicians',
        # Add more links for other genres if needed
    ]

    def parse(self, response):
        artist_links = response.css('div.div-col.columns.column-width ul li a[href^="/wiki/"]::attr(href)').getall()
        for link in artist_links:
            yield {
                'link': 'https://en.wikipedia.org' + link
            }

