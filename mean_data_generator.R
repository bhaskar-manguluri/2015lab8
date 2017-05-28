#!/usr/bin/env Rscript
a = sample(letters[1:10],size = 10000,replace = T)
b = rnorm(10000,30,4)
dataF = data.frame(a,b)
#write.csv(dataF,file = "mean_data.csv",row.names = F,col.names = NA)
# from documentation i cannot use col.names=NA argument
write.table(dataF,file = "mean_data.csv",row.names = F,col.names = F)
