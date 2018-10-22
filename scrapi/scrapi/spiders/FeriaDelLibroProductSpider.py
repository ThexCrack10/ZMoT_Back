# -*- coding: utf-8 -*-
import scrapy
from scrapi.items import FeriaDelLibroItem
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

class FeriaDelLibroProductSpider(scrapy.Spider):
  name = "LibrosDeals"
  allowed_domains = ["feriachilenadellibro.cl"]
  
  #Use working product URL below
  start_urls = [
     "https://www.feriachilenadellibro.cl/ciencias-sociales/la-elite-del-poder-mills-wright", "https://www.feriachilenadellibro.cl/ciencias-sociales/la-estructura-del-conflicto-redorta-josep",
     "https://www.feriachilenadellibro.cl/ciencias-sociales/el-arte-de-decir-no-kellner-hedwig", "https://www.feriachilenadellibro.cl/ciencias-sociales/todos-queremos-que-nos-quieran-lopez-juan-antonio"
     ]
 
  def parse(self, response):

    items = FeriaDelLibroItem()
    title = response.xpath('//*[@id="maincontent"]/div[2]/div[1]/div[1]/div[1]/div/h1/span/text()').extract()
    sale_price = response.xpath('//*[@id="maincontent"]/div[2]/div[1]/div[1]/div[2]/div[3]/span[1]/span/span/span/text()').extract()
    autor = response.xpath('//*[@id="maincontent"]/div[2]/div[1]/div[1]/div[1]/div/div/div/text()').extract()
    items['product_name'] = ''.join(title).strip()
    items['product_sale_price'] = ''.join(sale_price).strip()
    items['product_autor'] = ''.join(autor).strip()
    yield items

