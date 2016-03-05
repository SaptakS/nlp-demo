from earley import Earley
from bottomup import BottomUp
from topdown import TopDown
import nltk
import matplotlib.pyplot as plt

sentences = nltk.data.load('grammars/large_grammars/atis_sentences.txt')
sentences = nltk.parse.util.extract_test_sentences(sentences)
#sentences.sort(lambda x,y: cmp(len(x[0]), len(y[0])))
#print sentences
len_array = []
edges_array = []
time_earley_array = []
time_topdown_array = []
time_bottomup_array = []
for i in range(8):
	print "Iteration--->", i
	testsentence = sentences[i][0]
	len_array.append(len(testsentence))
	ep = Earley()
	edges_array.append(ep.parse(testsentence))
	time_earley_array.append(ep.time(testsentence))
	bu = BottomUp()
	time_bottomup_array.append(bu.time(testsentence))
	td = TopDown()
	time_topdown_array.append(td.time(testsentence))

plt.plot(len_array, time_earley_array, 'r--', len_array, time_topdown_array, 'b--')
plt.show()
