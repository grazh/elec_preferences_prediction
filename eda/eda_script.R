library(readxl)
library(lmtest)
library(corrplot)
library(ggplot2)
library(dplyr)
library(sandwich)
library(car)
library(robustbase)
library(caret)
library(stargazer)

rm(list = ls())

#
# Загрузим данные
#

Data <- data.frame(read_excel('students_data.xlsx'))
Data <- subset(Data, select=-c(...1))
View(Data)

colnames(Data)


#
# Изучим описательные статистики
#

S <- summary(Data)
S

# Корреляционная матрица
correlation1 <- cor(Data)

png(filename="corrgram.png")
corrplot(as.matrix(correlation1), method="number", sig.level=0.05,  tl.cex=1)
dev.off()
