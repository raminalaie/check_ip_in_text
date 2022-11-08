import re
data = [ "255.168.3.52 dsafds f",
      "1564653.355463.5463.46314",
      "dsa;fhd skfhla jfdiuh fudhcishf",
      "f sdljhfl 192.145.24.1",
      "dsfnhisdfk",
      "dfjshhfshkd"]

f = []
for i in data:
      p =i.split(" ")
      f.append(p)
# print(f)
def check(Ip):

	regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
	if(re.search(regex, Ip)):
		return 1
		
	else:
		return 0	
nah = [] 
    
for i in f:
      for j in i:
            nah.append(j)              
pp=[]

for j in nah:
      if check(j) == 1:
            pp.append(j)
            
print(pp)            