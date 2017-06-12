from mrjob.job import MRJob
import numpy as np
class mrmean(MRJob):

    def mapper(self,ikey,line):
        temp = line.split(',')
        key,value = temp
        key = key.strip('"')
        value = float(value)
        yield key,value

    def reducer(self,key,generator_of_values):
        sum = 0
        count = 0
        # why is this a generator,expected list Iterator
        for i in generator_of_values:
            sum = sum + i
            count = count + 1 
        
        avg = sum/count
        yield key,avg

if __name__ == "__main__":
    mrmean.run()
