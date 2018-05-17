import re

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
		#print(string)
		try:
			i = string[k]
		except IndexError:
			print(string)
			return ret
		if(i == ","):
			val = temp
			ret[key]=val
			temp = ""
			key = ""
			val = ""
			k += 1
			continue
		if(i == ":"):
			key = temp
			temp = ""
			k += 1
			if(string[k+1] == "{"):
				test = string[(k+1):]
				#print(test)
				li = [m.start() for m in re.finditer('}', test)]
				#print(li)
				v = ""
				li2 = [m.start() for m in re.finditer('{', test)]
				#print(li2)
				num = -1			
				for i in test:
					if(i == "{"):
						num = num + 1
					if(i == "}" and num == 0):
						v = v + i
						break
					if(i == "}"):
						num = num - 1
					v = v + i
				#print(v)
				temp = parse(v)
				print(v)
				string = string.replace(v,"")
			#print(key)
			continue	
		if(i == "{"):
			key = temp
			#temp = ""
			test = string[(k+1):]
			#index = test.find(",")
			#print(index)
			#if("{" in string.replace("{","") and "}" in string.replace("}","")):
			#	ret[key] = parse(test)
			#else:
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
	#print(ret)
	ret[key] = temp
	return ret	
