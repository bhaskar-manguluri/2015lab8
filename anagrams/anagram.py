from mrjob.job import MRJob
class anagram(MRJob):

    def mapper(self,key,value):
            yield ''.join(sorted(value)),value

    def reducer(self,key,wordlist):
        list = [word for word in wordlist]
        if len(list)>1:
            yield len(list),list

if __name__=='__main__':
    anagram.run() 
#anagram.run()
