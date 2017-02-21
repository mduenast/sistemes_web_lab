#!/usr/bin/env python
import urllib2

'''
Client web per www.udl.cat
@author mdt3@alumnes.udl.cat
'''

class Client(object):

        def __init__(self):
            pass

        def get_web(self,page):
            """ baixar-se la web """
            file = urllib2.urlopen(page)
            html = file.read()
            file.close()
            return html
        def main(self):
            # buscar el text
            # imprimir resultats
            web = self.get_web("http://www.udl.cat")
            print web
            pass

if __name__ == "__main__":
    client = Client()
    client.main()
