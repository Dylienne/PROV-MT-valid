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

#divide
ind <- sample(2, nrow(vcs), replace = TRUE, prob = c(0.6, 0.4))
train.data <- vcs[index== 1, ]
test.data <- vcs[index == 2, ]

#model 
myFormula <- labels ~ vcs$Days + vcs$VCS.Stars + vcs$WasInvalidatedBy

#tree 
ctree <- rpart(formula = myFormula, data = train.data, control= rpart.control(minsplit=5))

table(predict(ctree), vcs$Labels)
print(ctree)
plot(ctree)
table(vcs$Labels)
# reduce size of dataset to level of respondents and do it again. 
