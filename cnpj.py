#lfa

from pprint import pprint 
import requests
import threading
import json

class CnpjThread(threading.Thread):
    def __init__(self,cnpj):
        self.value = None
        self.cnpj = cnpj
        threading.Thread.__init__(self)

    def headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    def run(self):
        try:
            cnpj = self.cnpj.replace( "-", "" ).replace( ".", "" ).replace( "/", "" )
            url = 'http://receitaws.com.br/v1/cnpj/%s' %(cnpj)
            response = requests.get(url, headers=self.headers())
            self.value = json.loads(response.content.decode('utf-8'))
        except Exception as error:
            raise

    

cnpj = CnpjThread('27.865.757/0001-02')
cnpj.start()
cnpj.join()
pprint (cnpj.value)