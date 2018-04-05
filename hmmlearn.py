#correct code 
import math 
import json
import sys
with open(sys.argv[1],'r') as file:
	sentences = file.readlines()
tag_count = dict()
tag_count["start"]=len(sentences)
tag_count["finish"]=len(sentences)

def transition():
	tag_tag_count = dict()
	for i in range(len(sentences)):
		sentence = sentences[i].strip()
		sentence_split = sentence.split(" ")
		prev_tag = 'start'
		for j in range(len(sentence_split)):
			wordTag=sentence_split[j]
			tag = wordTag[wordTag.rindex('/')+1:]
			calcCount((prev_tag,tag),tag_tag_count)
			prev_tag=tag
		calcCount((prev_tag,'finish'),tag_tag_count)
	
	return tag_tag_count

def emission():
	tag_word_count = dict()
	for eachLine in sentences:
		eachLine = eachLine.strip()
		eachLine = eachLine.split(" ")
		for wordTag in eachLine:
			word = wordTag[0:wordTag.rindex('/')]
			tag = wordTag[wordTag.rindex('/')+1:]
			calcCount(tag,tag_count)
			calcCount((word,tag),tag_word_count)
	return tag_word_count
		

def calcCount(key,dictionary):
	if key in dictionary:
			dictionary[key] += 1
	else:
			dictionary[key] = 1

def calcProbability(dictionary1,dictionary2,em_or_tran):
	probability=dict()
	for keys in dictionary1:
		k1=keys[0]
		k2=keys[1]
		if(em_or_tran==1):
			probability[keys]=math.log((dictionary1[keys])/((dictionary2[k2])*1.0))
		else:
			probability[keys]=math.log((dictionary1[keys]+1)/((dictionary2[k1]+len(tag_count))*1.0))
			
	return probability

def allTags(dictionary):
	file = open('tags.txt','w') 
	c=0
	for keys in dictionary:
		if str(keys) !='start' and str(keys) !='finish':
			if c==len(dictionary)-1:
				file.write(str(keys)) 
			else:
				file.write(str(keys)+" ") 
		c+=1

def writeToFile(filename,dictionary):
	file=open(filename,'w')
	for keys in dictionary:
		k1=keys[0]
		k2=keys[1]
		value=dictionary[keys]
		file.write(k1+" "+k2+" "+str(value)+"\n")

def smoothning(row,column,dictionary):
	for s in row:
		for s1 in column:
			if (s,s1) not in dictionary:
				dictionary[(s,s1)]=math.log(1/((tag_count[s]+len(tag_count))*1.0))
		if ('start',s) not in dictionary:
			dictionary[('start',s1)]=math.log(1/((tag_count['start']+len(tag_count))*1.0))
		if (s,'finish') not in dictionary:
			dictionary[(s,'finish')]=math.log(1/((tag_count[s]+len(tag_count))*1.0))

	return dictionary

if __name__ == "__main__": 
	tag_tag_count=transition()
	tag_word_count=emission()
	#print tag_tag_count[('NN','finish')]
	transitionProb=calcProbability(tag_tag_count,tag_count,2)
	#print len(transitionProb)
	emissionProb=calcProbability(tag_word_count,tag_count,1)
	transitionProb=smoothning(tag_count,tag_count,transitionProb)
	#print len(transitionProb)
	#print len(emissionProb)
	writeToFile('transition.txt',transitionProb)
	writeToFile('emission.txt',emissionProb)
	allTags(tag_count)