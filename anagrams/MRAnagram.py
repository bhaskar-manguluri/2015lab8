from mrjob.job import MRJob

class MRAnagram(MRJob):

    def mapper(self,_,line):
        # Convert word into a list of characters,sort them,convert back to string
        letters = list(line)
        letters.sort()

        # key is the sorted word, value is the regular word
        yield letters,line

    def reducer(self,_,words):
        # Get the iterator of words for each key
        anagrams = [w for w in words]
        
        # only yield results if there are atleast two words which are anagrams of each other
        if len(anagrams) > 1:
            yield len(anagrams), anagrams


if __name__ == "__main__":
    MRAnagram.run()
