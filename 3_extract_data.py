#import re, os
substr = ['kind','collectionName', 'trackName', 'collectionPrice', 'trackPrice', 'primaryGenreName', 'trackCount', 'trackNumber', 'releaseDate']
fullname="t3.txt"
f = open(fullname, "r")
outt=""
fl=0
cou = 0
for text0 in f:
  text0 = f.readline()
  i=0
  while i<len(substr):
    b=text0.find(substr[i])
    if b == -1:
      outt=outt+" ,"    
    else:
#      print(str(substr[i]))
      if substr[i] == "releaseDate":
        outt=outt+(text0[b+len(substr[i])+2:]).split(',')[0].replace('T', ' ').replace('Z', '').replace('"', '')+","
      else:
        outt=outt+(text0[b+len(substr[i])+2:]).split(',')[0].replace('"', '')+","
#      print(text0[b+len(substr[i])+2:].strip('}'))
      fl+=1
    i+=1
  cou+=1
  if fl>0:
    print(outt.replace('}\n', '').rstrip(','))
    fl=0
  outt=""
f.close()
