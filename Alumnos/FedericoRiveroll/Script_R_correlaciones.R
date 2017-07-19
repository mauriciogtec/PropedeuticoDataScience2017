INEGI <- read.csv("/home/federico/Documents/MaestriaCienciaDatos/RepositorioProfesor/PropedeuticoDataScience2017/Datos/DatosINEGI.csv")
view(INEGI)

for(variable in c("Secundarias", "DefuncionesGenerales", "Nacimientos", "Divorcios", "Matrimonios")){
  INEGI[ , variable] <- INEGI[, variable] / INEGI[ ,"Poblacion"]
}

X <- INEGI[ ,-(1:2)] #Le quita las primeras dos columnas
row.names(X) <- INEGI$Estado
head(X)

# Ahora vamos a usar la paquetería FactoMiner para hacer componentes principales.

# install.packages("FactoMineR")

library(FactoMineR)

model <- PCA(X)