# -*- coding: utf-8 -*-
__version__ = '1.0'
__author__ = 'Aluen King Lee  (aluenkinglee@gmail.com)'
__web_site__ = 'http://www.aluenkinglee.com/blog'

'''
provide some functions that is more convient to present dict friendly

'''
import json
_a = {
"名字":"aluenkinglee",
"地址":{
    "城市":"北京",
    "街道":" 朝阳街",
    "邮编":100025,
    "location":"\u56db\u5ddd \u5e7f\u5143",
    },
"text":"python解析json中的unicode编码有点小麻烦阿"
}

print _a['地址'] 

_b=dict(_a)
_c=[0,1,2,3,4,23,4444,]

def _print_list(data):
    print '[',
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        print str(item) +',',
        if isinstance(item, list):
            item = _print_list(item)
        if isinstance(item, dict):
            item = _print_dict(item)
    print ']',

def _print_dict(data):
    print '{',
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        key_str = '\"' +str(key) +'\":'
        print key_str,
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        else:
            if isinstance(value,str) :
                print '\"'+value+'\",',
            elif  isinstance(value,int):
                print value,', ',
        if isinstance(value, list):
            value = _print_list(value)
        elif isinstance(value, dict):
            value = _print_dict(value)
    print '}',

def println_list(data):
    _print_list(data)
    print '\n',

def println_dict(data):
    _print_dict(data)
    print '\n',

def _decode_list_and_write(data,f):
    f.write("[")
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        f.write(item)
        f.write(',')
        if isinstance(item, list):
            item = _decode_list_and_write(item,f)
        if isinstance(item, dict):
            item = decode_dict_and_write(item,f)
    f.write(']')

def decode_dict_and_write(data,f):
    f.write("{")
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        key_str = '\"' +str(key) +'\":'
        f.write(key_str)

        if isinstance(value, unicode):
            value = value.encode('utf-8')
        else:
            if isinstance(value,str) :
                f.write('\"')
                f.write(value)
                f.write('\", ')
            elif  isinstance(value,int):
                f.write(str(value))
                f.write(', ')
        if isinstance(value, list):
            value = _decode_list_and_write(value,f)
        elif isinstance(value, dict):
            value = decode_dict_and_write(value,f)
    f.write('}')

def write_dict(data,f):
    decode_dict_and_write(data,f)
    f.write('\n')

def decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = decode_list(item)
        elif isinstance(item, dict):
            item = decode_dict(item)
        rv.append(item)
    return rv

def decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = decode_list(value)
        elif isinstance(value, dict):
            value = decode_dict(value)
        rv[key] = value
    return rv

def test():
    #--------------------------#
    f=open("test.txt","a+")
    decode_dict_and_write(_a,f)
    f.write("\n")
    f.close()

    #---------------------------#
    #same effect to statements above
    with open("test.dict","a+") as f:
        write_dict(_a,f)

    print _a['地址']
    println_dict(_a)
    bb = decode_dict(_b)
    println_dict(bb['地址'])


    println_list(_c)
    print _c

if __name__ == '__main__':  
    test()
