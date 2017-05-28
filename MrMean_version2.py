from mrjob.job import MRJob
#this gives different output to version 1,=> we cant use same combiner and reducer, because mean of means is different from mean of numbers , although they covert at large numbers
class mrmean(MRJob):

    def mapper(self,ikey,line):
        temp = line.split(',')
        key,value = temp
        key = key.strip('"')
        value = float(value)
        yield key,value

    def combiner(self,key,generator_of_values):
        sum = 0
        count = 0
        for i in generator_of_values:
            sum = sum + i
            count = count + 1 
        
        avg = sum/count
        yield key,avg

    def reducer(self,key,generator_of_values):
        sum = 0
        count = 0
        for i in generator_of_values:
            sum = sum + i
            count = count + 1 
        
        avg = sum/count
        yield key,avg


if __name__ == "__main__":
    mrmean.run()
