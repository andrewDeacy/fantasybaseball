__author__ = 'Andrew'
import connect
from rauth import OAuth1Service
from rauth.utils import parse_utf8_qsl
import pickle #key file pickled and then passed into connect file

def call_api(self, ):
keyfile = open('keyfile.txt', 'r')
connect.YahooAPI.__init__(self,keyfile,)

