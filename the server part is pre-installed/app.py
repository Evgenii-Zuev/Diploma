import urllib.request
link = urllib.request.urlopen('https://itunes.apple.com/search?term=The+Beatles')

lines = ""
for line in link.readlines():
  lines = lines + str(line)
link.close()

result = []
result = lines.split("}")

substr = ['kind','collectionName', 'trackName', 'collectionPrice', 'trackPrice', 'primaryGenreName', 'trackCount', 'trackNumber', 'releaseDate']
outt=""
fl=0
for text0 in result:
  i=0
  while i<len(substr):
    b=text0.find(substr[i])
    if b == -1:
      outt=outt+" ,"
    else:
      if substr[i] == "releaseDate":
        outt=outt+(text0[b+len(substr[i])+2:]).split(',')[0].replace('T', ' ').replace('Z', '').replace('"', '')+","
      else:
        outt=outt+(text0[b+len(substr[i])+2:]).split(',')[0].replace('"', '')+","
      fl+=1
    i+=1
  if fl>0:
    print(outt.replace('}\n', '').rstrip(','))
    fl=0
  outt=""