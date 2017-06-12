from mrjob.job import MRJob
class baseballLinks(MRJob):
    def mapper(self,_,line):
        row = line.split(',')                                                    
        name,own_team,friends_list = row[0],row[1],row[2:]
        friends_list.append(name)
        for friend in friends_list:
            friend = friend.strip()
            if friend ==name:
                special = "self_team"+own_team.lower()
                yield friend.lower(),special
            else:
                yield friend.lower(),own_team.lower()
        #yield name.lower(),"self_team"+own_team.lower()

    def reducer(self,key,list_of_team_links):
        self_team = None
        num_of_redsox_friends = 0
        num_of_cardinal_friends = 0
        check_self_team = 0
        for item in list_of_team_links:
            if item == " red sox":
                num_of_redsox_friends+=1
            elif item == " cardinals":
                 num_of_cardinal_friends+=1
            else:
                self_team = ""+item[10:]
               # check_self_team+=1
        yield(key,[self_team,num_of_redsox_friends,num_of_cardinal_friends])
          #  yield(key,item)

if __name__ == "__main__":
    baseballLinks.run()

