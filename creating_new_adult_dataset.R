
setwd("C:/Users/gokha/Desktop/data")
adult <- read.csv("ac.data", header = FALSE)




# Tests for different sample sizes (N) , I used them to test FP-growth but no Apriori

adult2=adult[1:5,]
adult3=adult[1:20,]
adult4=adult[1:100,]
adult5=adult[1:500,]
adult6=adult[1:1000,]
adult7=adult[1:2000,]
adult8=adult[1:5000,]
adult9=adult[1:10000,]
adult10=adult[1:20000,]

write.csv(adult2,'adult2.csv')
write.csv(adult3,'adult3.csv')
write.csv(adult4,'adult4.csv')
write.csv(adult5,'adult5.csv')
write.csv(adult6,'adult6.csv')
write.csv(adult7,'adult7.csv')
write.csv(adult8,'adult8.csv')
write.csv(adult9,'adult9.csv')
write.csv(adult10,'adult10.csv')




# Smaller  datasets with different sample size, I made them because Apriori does not work with large samples.
adultap5=adult[1:5,]
adultap10=adult[1:10,]
adultap15=adult[1:15,]
adultap20=adult[1:20,]
adultap30=adult[1:30,]
adultap40=adult[1:40,]
adultap50=adult[1:50,]
adultap60=adult[1:60,]
adultap70=adult[1:70,]
adultap75=adult[1:75,]
adultap80=adult[1:80,]
adultap90=adult[1:90,]
adultap100=adult[1:100,]


write.csv(adultap5,'adultap5.csv')
write.csv(adultap10,'adultap10.csv')
write.csv(adultap15,'adultap15.csv')
write.csv(adultap20,'adultap20.csv')
write.csv(adultap30,'adultap30.csv')
write.csv(adultap40,'adultap40.csv')
write.csv(adultap50,'adultap50.csv')
write.csv(adultap60,'adultap60.csv')
write.csv(adultap70,'adultap70.csv')
write.csv(adultap75,'adultap75.csv')
write.csv(adultap80,'adultap80.csv')
write.csv(adultap90,'adultap90.csv')
write.csv(adultap100,'adultap100.csv')



##################################################



# These datasets have same row repeated n times. All of them have N=100

adultp=adult[1,]



adultp1=do.call("rbind", replicate(10, adultp, simplify = FALSE))
adultp2=do.call("rbind", replicate(20, adultp, simplify = FALSE))
adultp3=do.call("rbind", replicate(30, adultp, simplify = FALSE))
adultp4=do.call("rbind", replicate(40, adultp, simplify = FALSE))
adultp5=do.call("rbind", replicate(50, adultp, simplify = FALSE))
adultp6=do.call("rbind", replicate(60, adultp, simplify = FALSE))
adultp7=do.call("rbind", replicate(70, adultp, simplify = FALSE))
adultp8=do.call("rbind", replicate(80, adultp, simplify = FALSE))
adultp9=do.call("rbind", replicate(90, adultp, simplify = FALSE))
adultp10=do.call("rbind", replicate(100, adultp, simplify = FALSE))

adultp1=rbind(adultp1, adult[2:91,])
adultp2=rbind(adultp2, adult[2:81,])
adultp3=rbind(adultp3, adult[2:71,])
adultp4=rbind(adultp4, adult[2:61,])
adultp5=rbind(adultp5, adult[2:51,])
adultp6=rbind(adultp6, adult[2:41,])
adultp7=rbind(adultp7, adult[2:31,])
adultp8=rbind(adultp8, adult[2:21,])
adultp9=rbind(adultp9, adult[2:11,])




write.csv(adultp1,'adultp1.csv')
write.csv(adultp2,'adultp2.csv')
write.csv(adultp3,'adultp3.csv')
write.csv(adultp4,'adultp4.csv')
write.csv(adultp5,'adultp5.csv')
write.csv(adultp6,'adultp6.csv')
write.csv(adultp7,'adultp7.csv')
write.csv(adultp8,'adultp8.csv')
write.csv(adultp9,'adultp9.csv')
write.csv(adultp10,'adultp10.csv')




summary(adultp10)
d=density(adultp7$V5)
plot(d)
hist(adultp10$V5)
sd(adultp10$V5)
mean(adultp10$V5)

sd(adultp7$V5)
mean(adultp7$V5)

var(adultp1$V5)
var(adultp2$V5)
var(adultp3$V5)
var(adultp4$V5)
var(adultp5$V5)
var(adultp6$V5)
var(adultp7$V5)
var(adultp8$V5)
var(adultp9$V5)
var(adultp10$V5)

hist(adultp8$V5)


########################################################
#Transaction size
adultt15=adult[1:100,]
adultt14=adult[1:100,1:14]
adultt13=adult[1:100,1:13]
adultt12=adult[1:100,1:12]
adultt11=adult[1:100,1:11]
adultt10=adult[1:100,1:10]
adultt9=adult[1:100,1:9]
adultt8=adult[1:100,1:8]
adultt7=adult[1:100,1:7]
adultt6=adult[1:100,1:6]
adultt5=adult[1:100,1:5]
adultt4=adult[1:100,1:4]
adultt3=adult[1:100,1:3]
adultt2=adult[1:100,1:2]
adultt1=adult[1:100,1]



write.csv(adultt15,'adultt15.csv')
write.csv(adultt14,'adultt14.csv')
write.csv(adultt13,'adultt13.csv')
write.csv(adultt12,'adultt12.csv')
write.csv(adultt11,'adultt11.csv')
write.csv(adultt10,'adultt10.csv')
write.csv(adultt9,'adultt9.csv')
write.csv(adultt8,'adultt8.csv')
write.csv(adultt7,'adultt7.csv')
write.csv(adultt6,'adultt6.csv')
write.csv(adultt5,'adultt5.csv')
write.csv(adultt4,'adultt4.csv')
write.csv(adultt3,'adultt3.csv')
write.csv(adultt2,'adultt2.csv')
write.csv(adultt1,'adultt1.csv')








############################################################################






library("readxl")
data=read_excel("deneme.xlsx")
plot(runtime~minsupport,data=data)
reg<-lm(runtime ~ minsupport, data = data)
summary(reg)

abline(reg, col="blue")