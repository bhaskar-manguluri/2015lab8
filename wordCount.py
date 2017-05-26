from mrjob.job import MRJob 
import re

class wordcount(MRJob):

     def mapper(self,key,line):
         for word in line.split('  '):
	     #wordi = re.sub('[^a-zA-Z]','',word)
             #word = ''.join(letter for letter in word if letter.isalpha())
             
             yield word.lower(),1

     def reducer(self,word,occurences):
         yield word,sum(occurences) 

if __name__=="__main__":
    wordcount.run()
