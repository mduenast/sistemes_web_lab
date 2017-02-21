#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup

'''
Client web per www.udl.cat
@author mdt3@alumnes.udl.cat
'''

class Client(object):

        def __init__(self,url):
            self.url = url

        def get_web(self,page):
            """ baixar-se la web """
            file = urllib2.urlopen(page)
            html = file.read()
            file.close()
            return html

        # TODO: buscar el text
        def search(self,html):
            soup = BeautifulSoup(html,'html.parser')
            elements = soup.find_all("div","featured-links-item")
            resultats = []
            for element in elements:
                data = element.find("time")["datetime"]
                title = element.find("span","flink-title")
                title = title.text if title else "Sense title"
                resultats.append((data,title))
            return resultats

        def main(self):
            # buscar el text
            # imprimir resultats
            web = self.get_web(self.url)
            resultat = self.search(web)
            #FIXME: imprimir resultats
            print resultat

if __name__ == "__main__":
    client = Client("http://www.udl.cat")
    client.main()
