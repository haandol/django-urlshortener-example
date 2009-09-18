#coding: utf-8

import re
from models import LongURL, ShortURL

BASE62 = '01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nBASE62 = len(BASE62)

PATTERN = r'http://[^/^\s]+[.]\w{2,4}\S*/?'

def get_short_id(url):
    u'''긴 URL을 받아서 짧은 URL의 id를 반환'''
    if not url:
        return WrongURL(0)
    elif not re.match(PATTERN, url):
        return WrongURL(1)

    longUrl, isnew = LongURL.objects.get_or_create(url=url)
    if isnew:
        id = encode_basen(longUrl.id)
        try:
            return ShortURL.objects.create(id=id, longUrl=longUrl).id
        except:
            raise WrongURL(2)
    else:
        try:
            return ShortURL.objects.get(longUrl=longUrl).id
        except ShortURL.DoesNotExist:
            raise ERROR(3)

def get_long_url(id):
    u'''아이디를 입력받아 인코딩한다'''
    try:
        return ShortURL.objects.get(id=id).longUrl.url
    except: 
        return ''

def encode_basen(id, n=nBASE62):
    u'''아이디를 입력받아 인코딩한다'''
    base = id
    rests = []
    while base!=0:
        quotient = base/n
        rests.append(BASE62[base%n])
        base = quotient

    return ''.join(rests)
