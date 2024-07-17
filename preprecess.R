# 예시 1
library(dplyr)
library(readxl)
library(reshape)
library(ggplot2)
setwd("C:\\Users\\삼성\\Desktop\\재성\\빅데이터 경진대회")
seoul = read_xlsx("연령_및_성별_인구__시군구_20211121185740.xlsx", sheet = 1)%>%
  data.frame(stringsAsFactors = F)
str(seoul)
head(seoul)
df = seoul[,c(2,3)]
str(df)
df = df[-1,]
str(df)
sigungu = unique(seoul[,1])
sigungu = sigungu[-c(1,3)]
sigungu2 = c()
for(i in 1:length(sigungu)){
  sigungu2[c((28*i - 27):(28*i))] = rep(sigungu[i],length(unique(df[,1])))
}
sigungu2
df2 = cbind(sigungu2,df)
df2
df2 = as.data.frame(df2)
colnames(df2) = c("구","연령","인구수")
head(df2)
str(df2)
df2$인구수 = as.numeric(df2$인구수)
dlsrntn = df2$인구수
over60 = c()
for(i in 1:length(sigungu)){
  over60[i] = sum(dlsrntn[c((28*i - 14):(28*i - 5))])
}
sigungu = c("전체","종로구","중구","용산구","성동구","광진구","동대문구",
            "중랑구","성북구","강북구","도봉구","노원구","은평구","서대문구",
            "마포구","양천구","강서구","구로구","금천구","영등포구","동작구",
            "관악구","서초구","강남구","송파구","강동구")
length(sigungu)
df3 = cbind(sigungu,over60)
df3 = as.data.frame(df3)
colnames(df3) = c("지역","노령인구수")
df3$노령인구수 = as.numeric(df3$노령인구수)
df3$지역 = gsub(' ','',df3$지역)
df3[2,1]
df4 = df3[-1,]
barplot(노령인구수~지역,df3)
write.csv(df3,file="서울 지역별 60세 이상 인구.csv")
# 예시 2
setwd("C:\\Users\\삼성\\Desktop\\재성\\빅데이터 경진대회")
library(dplyr)
library(readxl)
corona = read_xlsx("무상데이터상품_20200804.xlsx", sheet = 1)%>%
  data.frame(stringsAsFactors = F)
head(corona)

b = c("date","group","count")
colnames(corona) = b
head(corona)
tail(corona)

library(reshape)

corona2 = corona %>% arrange(date, group)
corona2
head(corona2)

a = data.frame((matrix(ncol = 3, nrow=length(corona2[,2]))))
for(i in 1:length(corona2[,2])){
  if(corona2[,2][i] == "스포츠/문화/레저"){
    a[i,] = corona[i,]
  }
}
f = na.omit(corona)
str(f)
tail(a)
str(a)
tail(corona)
corona3 = na.omit(a)
head(corona3)
rownames(corona3) = c(1:length(corona3[,1]))
colnames(corona3) = c("date","group","count")
head(corona3)
str(corona3)

tmp_d = data.frame((matrix(ncol = 1,nrow=length(corona3[,1]))))
library(ggplot2)
str(tmp_d)

for(i in 1:length(tmp_d[,1])){
  tmp_d[,1][i] = i
}
tmp_d[,1] = as.numeric(tmp_d[,1])
corona4 = cbind(tmp_d,corona3)
head(corona4)
head(corona4[,1])
colnames(corona4) = c("day","date","group","count")
str(corona4)


corona4$date = as.character(corona4$date)
corona4[,2] = as.Date(corona4[,2], format='%Y%m%d')