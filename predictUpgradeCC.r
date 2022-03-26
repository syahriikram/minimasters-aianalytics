#!/usr/bin/env Rscript
# Rscript test.r
library(rpart)
library(rpart.plot)

# reading data
d <- read.csv("CreditCardUpgrade.csv")
set.seed(2)

# labeling
d$Upgraded <- factor(d$Upgraded,  levels <- c(0,1), labels <- c("NoUp","YesUp"))
d$SuppCard <- factor(d$SuppCard,  levels <- c(0,1), labels <- c("No","Yes"))

# creating model
model <- rpart(d$Upgraded ~ d$Purchases + d$SuppCard, data <- d, control = rpart.control(minsplit = 2))
# model[["variable.importance"]]

# # optimize model
printcp(model)
model = prune(model, cp = 0.038462)
printcp(model)

# predict using model
pred <- predict(model, newdata <- d, type <- "class")
print(pred)

# check confusion matrix
confusion_matrix <- table(d$Upgraded, pred)
confusion_matrix

prp(model, type=2, extra=104, roundint=FALSE)
plotcp(model)
