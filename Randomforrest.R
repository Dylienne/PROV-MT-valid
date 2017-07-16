#Final calculations 
#Thesis M Information Sciences 
#By Dylienne Every VU University
#2127946
library(party)
library(partykit)
library(rpart)
library(randomForest)
library(Formula)

set.seed(2345)
#datasets 
vcs <- as.data.frame(filewithgrades)
respond <- provabbr
grades <- factor(vcs$Grade)
labels <- factor(vcs$Labels)
vcs$Days <-NULL

#divide
ind <- sample(2, nrow(vcs), replace = TRUE, prob=c(0.6, 0.4))
train.data <- vcs[ind==1, ]
test.data <- vcs[ind==2, ]

#random forrest
rf <- randomForest(labels~., data = vcs, ntree = 50, importance = T)
print(rf)
importance(rf)
varImpPlot(rf)

