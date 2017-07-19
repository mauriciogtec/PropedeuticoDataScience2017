install.packages("ggplot2")
library(ggplot2)
data(diamonds)
head(diamonds)

###Usaremos la función lm para hacer el ajuste de regresion, solo para las variables 'carat', 'depth', 'table', 'x' , 'y', 'z'


regres=lm(diamonds$price ~ diamonds$carat + diamonds$depth + diamonds$table + diamonds$x + diamonds$y + diamonds$z, data = diamonds)
summary(regres)

plot(regres)

sumacuadrados<- function(beta){
sum((diamonds$price - beta[1]- beta[2]*diamonds$carat - beta[3]*diamonds$depth - beta[4]*diamonds$table - beta[5]*diamonds$x - beta[6]*diamonds$y - beta[7]*diamonds$z)^2)
}

optim(c(20000,10000,-200,-100,-1300,50,50), sumacuadrados,hessian=TRUE)


sigma(regres)
