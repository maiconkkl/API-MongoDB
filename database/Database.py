import socket
from pymongo import MongoClient
from lxml import objectify


class Database:
    def __init__(self):
        f = open(r'C:\DigiSat\SuiteG6\Sistema\ConfiguracaoClient.xml', 'r')
        data = f.read()
        f.close()
        data = data.replace('<?xml version="1.0" encoding="utf-8"?>\n', '')
        data = data.replace('ï»¿', '')
        xml = objectify.fromstring(data)
        host = str(xml.Ip) if hasattr(xml, 'Ip') else '127.0.0.1'
        try:
            socket.inet_aton(host)
        except socket.error:
            try:
                host = socket.gethostbyname(host)
            except:
                host = '127.0.0.1'
        self.client = MongoClient(
            host=host, username='root', password='|cSFu@5rFv#h8*=',
            authSource='admin', port=12220, serverSelectionTimeoutMS=5000,
            connectTimeoutMS=10000, authMechanism='SCRAM-SHA-1'
        )

    def database_server(self):
        database = self.client['DigisatServer']
        return database

    def close_connection(self):
        self.client.close()
        return True