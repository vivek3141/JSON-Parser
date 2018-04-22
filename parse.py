#JSON Parser
def parse(string):
	string.replace("\n","")
	ret = {}
	temp = ""
	key = ""
	val = ""
	k = 0
	l = len(string)
	i = ""
	while(k<l):
		#print(ret)
		#print(i + " " + str(k) + " " + str(l))	
		l = len(string)
		if string == "{":
			return ret
		i = string[k]
		if(i == ","):
			val = temp[:]
			ret[key]=val
			temp = ""
			key = ""
			val = ""
			k += 1
			continue
		if(i == ":"):
			key = temp[:]
			#print(key)
			temp = ""
			k += 1
			continue	
		if(i == "{"):
			key = temp
			#temp = ""
			test = string[(k+1):]
			#print(test)
			if("{" in string.replace("{","") and "}" in string.replace("}","")):
				ret[key] = parse(test)
			else:
				#print("aA")
				ret = parse(test)
			string = string.replace(test,"")
			#print("String :" + string)
			val = ""
			key = ""
		if(i == "}"):
			ret[key] = temp
			return ret
		temp = temp + str(i)
		k += 1
	ret[key] = temp
	return ret	
