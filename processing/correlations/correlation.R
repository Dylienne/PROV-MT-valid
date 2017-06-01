library("reshape2")
library("ggplot2")

#correlations
datavcsrepo <- repository.data[, c(1,2,3,4)]
corr <- round(cor(data),2)
  
heatmap <- ggplot(data=meltcor, aes(x=Var1, y=Var2, fill=value)) + geom_tile()
databig <- repository.data[, c(1:20)]



> df <- as.data.frame(repository.data)
> provenance <- df[8:20]
> corpr <- round(cor(provenance) ,2)
> meltprov <- melt(corpr)
> heatmapprov <- ggplot(data=meltprov, aes(x=Var1, y=Var2, fill=value)) + geom_tile()
> 
  > heatmapprov