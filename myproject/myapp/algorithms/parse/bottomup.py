import nltk
from timeit import default_timer as timer

class BottomUp:

  def __init__(self, grammar = nltk.data.load('grammars/large_grammars/atis.cfg')):
    self.grammar = grammar

  def parse(self, sentence):
    parser = nltk.parse.BottomUpChartParser(self.grammar)
    chart = parser.chart_parse(sentence)
    print "BottomUp Parser Number of Edges::", chart.num_edges()

  def time(self, sentence):
  	start = timer()
	self.parse(sentence)
	end = timer()
	print(end - start) 
	return (end - start)
