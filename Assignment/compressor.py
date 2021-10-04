#Ex: wwwwaaadexxxxxx -> w4a3d1e1x6

def compress(data):
 encodedVersion = ""
 count = 1 
 for i in range(len(data)-1):
  if data[i] == data[i+1]:
    count += 1 
  else:
    encodedVersion += data[i] + str(count) 
    count = 1 
 encodedVersion += data[i] + str(count)
 return encodedVersion

print(compress("zzzzkkkkwwww")) 
