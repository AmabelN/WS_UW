#!/usr/bin/env python
# coding: utf-8

# ## Amabel Nabila
# ## 455854

# In[1]:


import scrapy

class MusiciansSpider(scrapy.Spider):
    name = "musicians"
    start_urls = [
        'https://en.wikipedia.org/wiki/50_Cent',
        # Add more links for other artists if needed
    ]

    def parse(self, response):
        band = response.css('table.infobox.vcard label::text').get()
        years_active = response.css('table.infobox.vcard tbody tr th:contains("Years active") + td::text').get()
        yield {
            'artist_name': response.css('h1#firstHeading::text').get(),
            'band': band.strip() if band else '',
            'years_active': years_active.strip() if years_active else ''
        }

