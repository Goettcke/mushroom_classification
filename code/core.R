---
  title: "Assignment 3"
  author : "Jonatan Møller Gøttcke"
  output: 
    html_document : 
    toc: TRUE
--- 
    
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```



library(rstudioapi)
#### Set working directory #### 
setwd(dirname(rstudioapi::getActiveDocumentContext()$path)) # This is for general case setting working directory. 

mushroom_data <- read.csv("../data/agaricus-lepiota.data", header = F )

target <- mushroom_data[,20]
target # Contains information the labels of the different mushrooms. 

