#anchormen onboarding with DecisionTree method 
# Fully written and developed by Dylienne Every - 06 1945 1993
# 13th of march 2017

library(rpart)
library(rattle)
library(RWeka)
library(caret)
library(party)
library(foreign)

#coversion .arff to .cvs
#temp = list.files(pattern="*.arff")
#for (i in 1:length(temp)) assign(temp[i], read.arff(temp[i]))
#for(i in 1:length(temp))
#{
  #mydata=read.arff(temp[i])
  #t=temp[i]
  #x=paste(t,".csv")
  #write.csv(mydata,x,row.names=FALSE)
 # mydata=0
#}

#variables utilized
data <- c(BreastCancerAll.reduced.using.cfs.arff.)
classcolumn <- data$class

#identification of preliminary features and rate of overfitting
str(data)
m1 <- J48(adm_data$class ~ ., data = adm_data)
summary(m1)

#visualization and classifier based on results and Kmean Error from Summary Rweka package

adm_data <- as.data.frame(data)
tree<- rpart(adm_data$class ~ ., data = adm_data, method = "class")

plot(tree)
text(tree, pretty =0)
printcp(tree)

#check the error margins from errorbars 
plotcp(tree)

#crossvalidation tenfold with random forrest 
model <- train(classcolumn ~ ., data,
  method = "rf",
  trControl = trainControl(
    method = "cv", number = 10,
    verboseIter = TRUE)
)
model

#prunetree + validation to compare with random forrest 
# insert formula of cross validated parameters first 
J48(data$class ~ . , data= adm_data, control= Weka_control(M=1,U=FALSE))

# summary embedded - LEAVE DYLIE 
evaluate_Weka_classifier(m1, numFolds = 10, seed = 123, class = TRUE)
m1 <- J48(adm_data$class ~ ., data = adm_data)
m1

# just for insight
#plot heaviest leaves - to see weight and important factors 
heavyleaves1 <- BreastCancerAll.reduced.using.cfs.arff.$X4322_chrom8_reg184617.320897_probnorm
heavyleaves2 <- BreastCancerAll.reduced.using.cfs.arff.$X1471_chrom2_reg131945577.132042781_probgain
heavyleaves3 <- BreastCancerAll.reduced.using.cfs.arff.$X7317_chrom12_reg72645832.73482351_probloss

m2 <- J48(classcolumn ~ heavyleaves3 + heavyleaves2 + heavyleaves1)
evaluate_Weka_classifier(m1)
if(require("party", quietly = TRUE)) 
  plot(m2)
