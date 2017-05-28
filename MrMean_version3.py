from mrjob.job import MRJob
#this is another false way to add combiner
# 
class mrmean(MRJob):

    def mapper(self,ikey,line):
        temp = line.split(',')
        key,value = temp
        key = key.strip('"')
        value = float(value)
        #yield key,value
        #yield changed to let it match combiner output/reduce input
        yield key,(value,1)

    def combiner(self,key,tuple_list):
        sum = 0
        count = 0
        for part_sum,part_count in tuple_list:
            sum = sum + part_sum
            count = count + part_count 
        yield key,(sum,count)

    def reducer(self,key,tuple_list):
        sum = 0
        count = 0
        for part_sum,counts in tuple_list:
            sum = sum + part_sum
            count = count + counts 
        
        avg = sum/count
        yield key,avg


if __name__ == "__main__":
    mrmean.run()
#there will be very very small diff between output of version1 and version3 due to decimal approximation of sum in combiner in version3 where as in case of version1 only decimal approximation is in reducer

