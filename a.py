#!/usr/bin/env python
# encoding: utf-8
def test(a):
    if(a!="a"):
      raise Exception("dddddddddd")
    return

def test2():
     a = "1|2".split("|")
     b = "1|3".split("|")
     c = "4|5".split("|")
	 d = "dsdfd|ddd".split("1")
     al=[]
     al.extend(b)
     al.extend(c)
     al= list(set(al))
     for ip in al :
         print(ip)

def aaa(serverName):
    if "tt"==serverName:
        return "kk"
    else:
        return "aaaaa"

if __name__ == '__main__':
   print(aaa("tt"))