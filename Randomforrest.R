#Final calculations 
#Thesis M Information Sciences 
#By Dylienne Every VU University
#2127946
library(party)
library(partykit)
library(rpart)
library(randomForest)
library(Formula)
library(caret)
library(mlbench)


set.seed(2345)
#datasets 
vcs <- as.data.frame(filewithgrades)
cleanvcs <- vcs[sample(nrow(vcs), 32), ]
#grades <- factor(vcs$Grade)
labels <- factor(vcs$Labels)
#vcs$Days <-NULL

#Feature engineering
cleanrespo <- dummies
total_df <- merge(cleanrespo, cleanvcs)
labels_full <- total_df$Labels
names(total_df)[names(total_df) == "I.think.that.the.more.collaborators.are.involved.in.a.project..the.more.efficient.the.code.and.repository.will.yield.to.be." ] <- "collabs"
names(total_df)[names(total_df) == "Customer.Relationship.Management.System_Customer.Relationship.Management.System" ] <- "Platform"


#divide
ind <- sample(2, nrow(total_df), replace = TRUE, prob=c(0.6, 0.4))
train.data <- total_df[ind==1, ]
test.data <- total_df[ind==2, ]
#total_df$Labels <- NULL 
#total_df$Grade <- NULL

#cross validation because it is a small dataset 
control <- trainControl(method='repeatedcv', number =10, repeats=2)
model <- train(labels_full ~.,
                total_df$VCS.Commits 
               , data=total_df, method='rf', preProcess ="scale", 
               trControl = control
               , importance = TRUE)

#random forrest
rf <- randomForest(labels_full ~.,total_df$VCS.Commits, data = total_df, ntree = 100, importance = T)
              
                 
print(rf)
importance(rf)
varImpPlot(rf)
print(model)

#model assesment 


# Tree Random forrest cross validation 





