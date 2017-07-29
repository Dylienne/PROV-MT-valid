#variable importance
set.seed(2343)
library('mlbench')
library('caret')
library('randomForest')

data <- dummies
df <- filewithgrades


grade <- filewithgrades$Grade
grade <- grade[1:32]

control <- trainControl(method='repeatedcv', number =10, repeats=2)
model <- train(grade ~., data=dummies, method='rf', preProcess ="scale", 
               trControl = control
               , importance = TRUE)
importance <- varImp(model, scale = FALSE)

print(importance)
plot(importance)

print(model)

