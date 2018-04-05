#correct code best accuracy 
import json
import operator

file = open("/Users/namanapawar/Downloads/coding1-data-corpus/en_dev_raw.txt")
tagFile = open("/Users/namanapawar/Desktop/tags.txt")
transhitionProbFile = open("/Users/namanapawar/Desktop/transition.txt")
emissionProbemFile = open("/Users/namanapawar/Desktop/emission.txt")
constant=-9999999999999999
tagList = []
wordList=set()
outfile = open("hmmoutput.txt","w") 
outputStringLine=''

def createTagList():
	tags=tagFile.readlines()
	for tag in tags:
		tag=tag.split(" ")
		for i in tag:
		    tagList.append(i)

def createDictionary(fileName,add):
	dictionary=dict()
	lines=fileName.readlines()
	for line in lines:
		line=line.strip();
		line=line.split(" ")
		dictionary[(line[0],line[1])]=float(line[2])
		if add:
			wordList.add(line[0])
	return dictionary

				
def viterbiAlgo(observations,state_graph):
	global outputStringLine
	T=len(observations)
	N=len(state_graph)
	viterbi=list()
	backpointer=list()
	for i in range(N):
		backpointer.append([None]*T)
		viterbi.append([None]*T)

	for s in range(0,N):
		tKey=('start',state_graph[s])
		eKey=(observations[0],state_graph[s])
		if observations[0] in wordList:
			if eKey in emissionProb:
				viterbi[s][0] = transitionProb[tKey]+emissionProb[eKey]
				backpointer[s][0]=0
				#print tKey, viterbi[s][0]
			else:
				viterbi[s][0] = transitionProb[tKey]+constant
		else:
			viterbi[s][0] = 2*transitionProb[tKey]
			backpointer[s][0]=0
			#print tKey, viterbi[s][0]
    
	

	for t in range(1,T):
		for s in range(0,N):
			max_value = float("-inf")

			for s1 in range(0,N):
				tKey=(state_graph[s1],state_graph[s])
				eKey=(observations[t],state_graph[s])
				if observations[t] in wordList and viterbi[s1][t-1] is not None:
					if eKey in emissionProb:
						intermediate = viterbi[s1][t-1]+transitionProb[tKey]+emissionProb[eKey]
						if max_value < intermediate:
							max_value = intermediate
						#print tKey,eKey,inter_result
					else:
						intermediate = viterbi[s1][t-1]+transitionProb[tKey]+constant
						if max_value < intermediate:
							max_value = intermediate
				else:
					if viterbi[s1][t-1] is not None:
						intermediate = viterbi[s1][t-1]+(2*transitionProb[tKey])
						if max_value < intermediate:
							max_value = intermediate
					#print tKey,eKey,inter_result
			

			if max_value!=float("-inf"):
				viterbi[s][t]=max_value

			max_value = float("-inf")
			prev_index = -1

			for s1 in range(0,N):
				tKey=(state_graph[s1],state_graph[s])
				if viterbi[s1][t-1] is not None:
					intermediate=viterbi[s1][t-1]+transitionProb[tKey]
					if max_value < intermediate:
						max_value = intermediate
						prev_index = s1 

			if max_value != float("-inf"):
				backpointer[s][t] = prev_index
			else:
				backpointer[s][t] = -1
	
	max_value = float("-inf")
	prev_index = -1
	count=0
	for s in range(0,N):
		key=(state_graph[s],'finish')
		if viterbi[s][T-1] is not None:
				inter_result =  viterbi[s][T-1]+transitionProb[key]
				#print count,key, inter_result
				count+=1
				if max_value < inter_result:
					max_value = inter_result
					prev_index = s

	if max_value !=  float("-inf"):
		viterbi[N-1][T-1] = max_value 
		backpointer[N-1][T-1]= prev_index
	else:
		backpointer[N-1][T-1] = -1

	row=N-1
	col=T-1
	#print observations[T-1],state_graph[backpointer[N-1][T-1]]
	outputStringLine=observations[T-1]+"/"+state_graph[backpointer[N-1][T-1]]+" "
	row = backpointer[backpointer[N-1][T-1]][T-1]
	for i in range(T-1,0,-1):
		#print observations[i-1]+"/"+state_graph[backpointer[row][i]]
		outputStringLine+=observations[i-1]+"/"+state_graph[backpointer[row][i]]+" "
		#print observations
		#outfile.write(observations[i-1]+"/"+state_graph[backpointer[row][i]]+" ")
		row=backpointer[backpointer[row][i]][i-1]

def reverseWords(input):
    inputWords = input.split(" ")
    inputWords=inputWords[-1::-1]
    output = ' '.join(inputWords)
    output=output[1:]
    return output


createTagList()
transitionProb=createDictionary(transhitionProbFile,False)
emissionProb=createDictionary(emissionProbemFile,True)
lines=file.readlines()
print len(wordList)
for line in lines:
	line=line.strip()
	line=line.split(" ")
	viterbiAlgo(line,tagList)
	outputStringLine=reverseWords(outputStringLine)
	outfile.write(outputStringLine+"\n")
	outputStringLine=''

'''
line="From the AP comes this story :"
line=line.strip()
line=line.split(" ")
viterbiAlgo(line,tagList)
'''







