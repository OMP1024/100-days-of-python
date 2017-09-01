# -*- coding: utf-8 -*-
__author__ = 'abbot'

import json
import chardet

strList = '[1,2,3,4]'
strDict = '{"city":"北京","name":"天安门"}'

j = json.loads(strList)
print(j)

dictJ = json.loads(strDict)
print(dictJ)

listStr = [1,2,3,4]
tupleStr = (1,2,3,4)
dictStr = {"city":"北京","name":"天安门"}

print(json.dumps(listStr))

print(json.dumps(tupleStr))



print(json.dumps(dictStr,ensure_ascii=False))


listStr = [{"city": "北京"}, {"name": "大刘"}]
json.dump(listStr, open("listStr.json","w"), ensure_ascii=False)

dictStr = {"city": "北京", "name": "大刘"}
json.dump(dictStr, open("dictStr.json","w"), ensure_ascii=False)
