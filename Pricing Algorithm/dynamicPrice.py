# designed by Xianglong Feng & Chunhua Deng & Siyu Liao

import csv
import numpy as np
from scipy.optimize import leastsq
import math
import matplotlib.pyplot as plt
'''import pandas as pd'''

'''hourly processing'''
'''
csv_reader = csv.reader(open("hourly.csv"))
for row in csv_reader:
    print(row)
'''
'''

###采样点(Xi,Yi)###
Xi=np.array([8.19,2.72,6.39,8.71,4.7,2.66,3.78])
Yi=np.array([7.01,2.78,6.47,6.71,4.1,4.23,4.05])

###The finction that could fit :func  & error###
def func(p,x):
    k,b=p
    return k*x+b
### ============================modifid by Xianglong Feng==============================
def error(p,x,y,s):
    print (s)
    return func(p,x)-y #x、y are list，The return is also a list

#TEST
p0=[100,2]
#print( error(p0,Xi,Yi) )

###主函数从此开始###
s="Test the number of iteration" #试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的k、b
Para=leastsq(error,p0,args=(Xi,Yi,s)) #把error函数中除了p以外的参数打包到args中
k,b=Para[0]
print("k=",k,'\n',"b=",b)

###绘图，看拟合效果###


plt.figure(figsize=(8,6))
plt.scatter(Xi,Yi,color="red",label="Sample Point",linewidth=3) #画样本点
x=np.linspace(0,10,1000)
y=k*x+b
plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2) #画拟合直线
plt.legend()
plt.show()





###采样点(Xi,Yi)###
Xi=np.array([0,1,2,3,-1,-2,-3])
Yi=np.array([-1.21,1.9,3.2,10.3,2.2,3.71,8.7])

###需要拟合的函数func及误差error###
def func(p,x):
    a,b,c=p
    return a*x**2+b*x+c

def error(p,x,y,s):
    print (s)
    return func(p,x)-y #x、y都是列表，故返回值也是个列表

#TEST
p0=[5,2,10]
#print( error(p0,Xi,Yi) )

###主函数从此开始###
s="Test the number of iteration" #试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的a~c
Para=leastsq(error,p0,args=(Xi,Yi,s)) #把error函数中除了p以外的参数打包到args中
a,b,c=Para[0]
print("a=",a,'\n',"b=",b,"c=",c)

###绘图，看拟合效果###


plt.figure(figsize=(8,6))
plt.scatter(Xi,Yi,color="red",label="Sample Point",linewidth=3) #画样本点
x=np.linspace(-5,5,1000)
y=a*x**2+b*x+c
plt.plot(x,y,color="orange",label="Fitting Curve",linewidth=2) #画拟合曲线
plt.legend()
plt.show()
 
'''

'''
tmp=np.loadtxt("hourlyB.csv",dtype=np.str,delimiter=',')
print("======temp=======")
print(tmp)
print("=================")
'''

'''
'
data = tmp[1:,1:].astype(np.float)#加载数据部分
label = tmp[1:,0].astype(np.float)#加载类别标签部分

print("======data=======")
print(data)
print("=================")

print("======label=======")
print(label)
print("=================")
'''

'''
data = pd.read_csv("hourly.csv")
print(data)

data = pd.read_table("hourly.csv",sep=",")
print(data)
'''

'''============monthly============='''
HYi=np.array([15485.66667,52141.5,130229,331530.6667,615963.8333,795178.3333,940447.8333,1051075.833,1069289,983252.1667,902227.8333,858054.3333,861664.8333,828231.1667,594097.8333,300653.1667,3649,3022.666667,7269.166667,5600.833333,3950,2712.833333,2325,3755.166667])
HXi=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])

#HYi=np.array([15485.66667,52141.5,130229,331530.6667,615963.8333,795178.3333,940447.8333,940447.8333,940447.8333,940447.8333,902227.8333,858054.3333,902227.8333,858054.3333,594097.8333,300653.1667,3649,3022.666667,7269.166667,5600.833333,3950,2712.833333,2325,3755.166667])
#HXi=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])

MYi=np.array([823986.8333,820729.3333,953762.1667,915111.5,914880.1667,941198.1667,933621.3333,982761.3333,882405.3333,947825.8,814295.2,867021.6])
MXi=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

WYi=([1573677,1798842.8,1819455.6,1831268.8,1942444,1826030.2,4685])
WXi=np.array([1,2,3,4,5,6,7])
###采样点(Xi,Yi)###
Xi=np.array([0,1,2,3,-1,-2,-3])
Yi=np.array([-1.21,1.9,3.2,10.3,2.2,3.71,8.7])

#BasicPrice is BP=2.5
BP=2.5
###需要拟合的函数func及误差error###
def func(p,x):
    a,b,c,d,e,f,g=p
    return a*x**6+b*x**5+c*x**4+d*x**3+e*x**2+f*x+g

def error(p,x,y,s):
    print (s)
    return func(p,x)-y #x、y都是列表，故返回值也是个列表

#TEST initialize the a b c d
p0=[1,1,1,1,1,1,1]
#print( error(p0,Xi,Yi) )

# for week
plt.figure(figsize=(8,6))
s="Test the number of iteration" #试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的a~c
Para=leastsq(error,p0,args=(WXi,WYi,s))
a,b,c,d,e,f,g=Para[0]
print("a=",a,'\n',"b=",b,"c=",c)
plt.scatter(WXi,WYi,color="red",label="Real dataset",linewidth=3) #画样本点
Wx=np.linspace(1,7,1000)
Wy=a*Wx**6+b*Wx**5+c*Wx**4+d*Wx**3+e*Wx**2+f*Wx+g
plt.plot(Wx,Wy,color="orange",label="Fitting Curve",linewidth=2) #画拟合曲线

font2 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 14,
}
plt.xlabel('Days in a Week',font2)
plt.ylabel('Numbers of parking user',font2)

plt.legend()
plt.show()


###主函数从此开始###
s="Test the number of iteration" #试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的a~c
Para=leastsq(error,p0,args=(HXi,HYi,s)) #把error函数中除了p以外的参数打包到args中
#Para=leastsq(error,p0,args=(MXi,MYi,s))
#Para=leastsq(error,p0,args=(WXi,WYi,s))
a,b,c,d,e,f,g=Para[0]
print("a=",a,'\n',"b=",b,"c=",c)

###绘图，看拟合效果###


plt.figure(figsize=(8,6))
plt.scatter(HXi,HYi,color="red",label="Real dataset",linewidth=3) #画样本点
#x=np.linspace(1,12,1000)
x=np.linspace(0,24,1000)

y=a*x**6+b*x**5+c*x**4+d*x**3+e*x**2+f*x+g
plt.plot(x,y,color="orange",label="Fitting Curve",linewidth=2) #画拟合曲线

x=np.linspace(0,24,1000)
y=(1*a*x**6+1*b*x**5+1*c*x**4+1*d*x**3+1*e*x**2+f*x)/(0.2*x+1)+g+0.25
#plt.plot(x,y,color="blue",label="Price",linewidth=2) #画拟合曲线

font2 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 14,
}
plt.xlabel('Hours in a day',font2)
plt.ylabel('Numbers of parking user',font2)
plt.legend()
plt.show()

'''append the first segment'''
PDX=np.linspace(0,2,200)
PDY=a*PDX**6+b*PDX**5+c*PDX**4+d*PDX**3+e*PDX**2+f*PDX+g
'''test the 5 segment adjustment'''
'''This part is the 2nd '''
PX=np.linspace(2,5,300)
PY=a*PX**6+b*PX**5+c*PX**4+d*PX**3+e*PX**2+f*PX+g
plt.figure(figsize=(8,6))
#plt.plot(PX,PY,color="blue",label="new curve",linewidth=2) #画拟合曲线
Pmax=max(PY)
Pmin=min(PY)
PY=PY/Pmax
CoA=Pmax
PAX=np.linspace(2,5,300)
PAX=PAX/24
C=1
B=0
PAY= -C * ( PAX*PAX*PAX*PAX*PAX*PAX- 1) + B   # easeOutQuart
NPY=PY*PAY
RNPY=NPY[::-1]
#RNPY=RNPY*RNPY
NewPY=(NPY+RNPY)/2
NewCoePY= -C * ( PY*PY*PY*PY- 1) + B
NewCoePY=NewCoePY*0.3
NewPY=(PY+NewCoePY)
plt.plot(PX,PY,color="red",label="Original curve",linewidth=2) #画拟合曲线
#plt.plot(PX,RNPY,color="blue",label="modified index curve",linewidth=2) #画拟合曲线
#plt.plot(PX,NewCoePY,color="orange",label="modified coeff curve",linewidth=2) #画拟合曲线
plt.plot(PX,NewPY,color="green",label="Modified final curve",linewidth=2) #画拟合曲线

font2 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 14,
}
plt.xlabel('Hours in a day',font2)
plt.ylabel('Scaled numbers of parking user',font2)
plt.legend()
plt.show()



'''test the 5 segment adjustment'''
'''This part is the 3rd'''
#PBX=np.linspace(5,17,1200)
PBX=np.linspace(2,21,1900)
PBY=a*PBX**6+b*PBX**5+c*PBX**4+d*PBX**3+e*PBX**2+f*PBX+g
plt.figure(figsize=(8,6))
#plt.plot(PX,PY,color="blue",label="new curve",linewidth=2) #画拟合曲线
Pmax=max(PBY)
Pmin=min(PBY)
PBY=PBY/Pmax
CoB=Pmax
PBYco=1-PBY
PBYNew=(PBYco/2+PBY)
#PBAX=np.linspace(5,17,1200)
PBAX=np.linspace(2,21,1900)
PBAX=PAX/24
C=1
B=0
PBYC=PBY*0.6
PBYcoe= -C * ( PBYC*PBYC*PBYC*PBYC- 1) + B   # easeOutQuart
PBYFinal=(PBYcoe+PBYNew)/2
#NPY=PY*PAY
#RNPY=NPY[::-1]
#RNPY=RNPY*RNPY
#NewPY=(NPY+RNPY)/2
#NewCoePY= C * ( PBY*PBY*PBY*PBY- 1) + B
#NewCoePY=NewCoePY*0.3
#NewPY=(PY+NewCoePY)
plt.plot(PBX,PBY,color="red",label="original curve",linewidth=2) #画拟合曲线
#plt.plot(PBX,PBYco,color="blue",label="modified index curve",linewidth=2) #画拟合曲线
#plt.plot(PBX,PBYNew,color="orange",label="modified coeff curve",linewidth=2) #画拟合曲线
plt.plot(PBX,PBYFinal,color="green",label="modified final curve",linewidth=2) #画拟合曲线
#plt.plot(PBX,PBYcoe,color="Black",label="coeff final curve",linewidth=2) #画拟合曲线

font2 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 14,
}
plt.xlabel('Hours in a day',font2)
plt.ylabel('Scaled numbers of parking user',font2)
plt.legend()
plt.show()



'''test the 5 segment adjustment'''
'''This part is the 4rd'''
PCX=np.linspace(17,21,400)
PCY=a*PCX**6+b*PCX**5+c*PCX**4+d*PCX**3+e*PCX**2+f*PCX+g
plt.figure(figsize=(8,6))
#plt.plot(PX,PY,color="blue",label="new curve",linewidth=2) #画拟合曲线
Pmax=max(PCY)
Pmin=min(PCY)
PCY=PCY/Pmax
CoC=Pmax
RNPCY=PCY[::-1]
#RNPY=RNPY*RNPY
NewPCY=(PCY+RNPCY)/2
NewCoePCY= -C * ( PCY*PCY*PCY*PCY- 1) + B
NewCoePCY=NewCoePCY*0.3
NewPCY=(PCY+NewCoePCY)
plt.plot(PCX,PCY,color="red",label="original curve",linewidth=2) #画拟合曲线
#plt.plot(PCX,RNPCY,color="blue",label="modified index curve",linewidth=2) #画拟合曲线
#plt.plot(PCX,NewCoePCY,color="orange",label="modified coeff curve",linewidth=2) #画拟合曲线
plt.plot(PCX,NewPCY,color="green",label="modified final curve",linewidth=2) #画拟合曲线

font2 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 14,
}
plt.xlabel('Hours in a day',font2)
plt.ylabel('Scaled numbers of parking user',font2)
plt.legend()
plt.show()

'''append the last segment'''
PEX=np.linspace(21,24,300)
PEY=a*PEX**6+b*PEX**5+c*PEX**4+d*PEX**3+e*PEX**2+f*PEX+g

'''time based demand function'''
XX=np.linspace(0,24,2400)
YY=a*XX**6+b*XX**5+c*XX**4+d*XX**3+e*XX**2+f*XX+g
COMYY=max(YY)
NormYY=YY/COMYY
#NewYY=np.append(PDY,NewPY,PBYFinal,NewPCY,PEY)
#NewYY=np.append([PDY,NewPY,PBYFinal])
#NewYY=np.concatenate([PDY,NewPY*CoA,PBYFinal*CoB*0.9,NewPCY*CoC,PEY])
NewYY=np.concatenate([PDY,PBYFinal*CoB*0.9,PEY])
COMNewYY=max(NewYY)
NormNewYY=NewYY/COMNewYY
NewNormNewYY=NormNewYY*NormYY
#NewNormNewYY=math.sqrt(NewNormNewYY)
NewNormNewYY=NewNormNewYY*COMNewYY

TryNewYY=NewYY-YY
TryNewYY=(TryNewYY+abs(TryNewYY))/2
#TryNewYY=abs(NewYY-TryNewYY)
FirstMax=0
for i in range(len(TryNewYY)):
    if  i<= 205:
        TryNewYY[i] = YY[i]
    else:
        if TryNewYY[i] > 0:
            if i> 200 and i<1100:
                TryNewYY[i] = COMNewYY - TryNewYY[i]
                if TryNewYY[i]-YY[i]>FirstMax:
                    FirstMax=TryNewYY[i]-YY[i]
                TryNewYY[i]=YY[i]+(FirstMax-(TryNewYY[i]-YY[i]))
                if TryNewYY[i]>=NewYY[i]:
                    TryNewYY[i]=NewYY[i]

            elif i> 1100 and i<2100:
                TryNewYY[i] = COMNewYY - TryNewYY[i]
                if TryNewYY[i]-YY[i]>FirstMax:
                    FirstMax=TryNewYY[i]-YY[i]
                TryNewYY[i]=YY[i]+(FirstMax-(TryNewYY[i]-YY[i]))
                if TryNewYY[i]>=NewYY[i]:
                    TryNewYY[i]=NewYY[i]
        else:
            TryNewYY[i] = NewYY[i]

plt.figure(figsize=(8,6))
plt.plot(XX,YY,color="orange",label="original curve",linewidth=2) #画拟合曲线
plt.plot(XX,TryNewYY,color="green",label="modified curve",linewidth=2) #画拟合曲线
#plt.plot(XX,NewYY,color="blue",label="modified curve",linewidth=2) #画拟合曲线

font2 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 14,
}
plt.xlabel('Hours in a day',font2)
plt.ylabel('Numbers of parking user',font2)
plt.legend()
plt.show()

'''price compairation'''
plt.figure(figsize=(8,6))
XXP=np.ones(2400)
YYP=XXP*2.5
YYPNew=XXP*2.5
startNO=400
for i in range(len(TryNewYY)):
    if TryNewYY[i] > YY[i]:
        if i<startNO:
            startNO=i
        if i<1100:
            YYPNew[i]= ( -C * ( (1-NormYY[i])*(1-NormYY[i])*(1-NormYY[i])*(1-NormYY[i])*(1-NormYY[i])*(1-NormYY[i])- 1) + B) *YYP[i]
        elif i<2000:
            YYPNew[i] = (-C * (
                        (1 - NormYY[i]) * (1 - NormYY[i]) * (1 - NormYY[i]) * (1 - NormYY[i]) * (1 - NormYY[i]) * (
                            1 - NormYY[i]) - 1) + B) * YYP[i]
    if TryNewYY[i] < YY[i]:
        if i>200 and i<2000:
            YYPNew[i]= (C * ((NormYY[i]) * ( NormYY[i]) * (NormYY[i]) * (NormYY[i]) * (NormYY[i]) * (NormYY[i]) - 1) + B +2)* YYP[i]
plt.plot(XX,YYP,color="orange",label="fixed price",linewidth=2) #画拟合曲线
plt.plot(XX,YYPNew,color="green",label="dynamic price",linewidth=2) #画拟合曲线
font2 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 14,
}
plt.xlabel('Hours in a day',font2)
plt.ylabel('Parking price',font2)

plt.legend()
plt.show()


price=np.linspace(0,1,24)
countInd=0
countP=0
for i in range(len(YYPNew)):
    countInd=countInd+1
    if countInd==100:
        countInd=0
        price[countP]=YYPNew[i]
        countP=countP+1

'''Benifits compairation'''
plt.figure(figsize=(8,6))
YYBeni=XXP*0
YYBeniNe=XXP*0

YY=YY/1000000  # million
TryNewYY=TryNewYY/1000000  #million

for i in range(len(XX)):
    if i==0:
        YYBeni[i]=YYP[i]*YY[i]
        YYBeniNe[i]=YYPNew[i]*TryNewYY[i]
    else:
        YYBeni[i] = YYP[i] * YY[i]+YYBeni[i-1]
        YYBeniNe[i] = YYPNew[i] * TryNewYY[i]+YYBeniNe[i-1]
plt.plot(XX,YYBeni,color="orange",label="fixed benifite",linewidth=2) #画拟合曲线
plt.plot(XX,YYBeniNe,color="green",label="dynamic benifite",linewidth=2) #画拟合曲线
font2 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 14,
}
plt.xlabel('Hours in a day',font2)
plt.ylabel('Final benefites (Million)',font2)

plt.legend()
plt.show()


''''
plt.figure(figsize=(8,6))
#plt.scatter(MXi,MYi,color="red",label="Sample Point",linewidth=3) #画样本点
x=np.linspace(0,1,1000)
y=0.001*x**(-1)
plt.plot(x,y,color="orange",label="Fitting Curve",linewidth=2) #画拟合曲线
x=np.linspace(0,1,1000)
y=(1-x)
plt.plot(x,y,color="red",label="Fitting Curve",linewidth=2) #画拟合曲线
'''

'''
x=np.linspace(1,24,1000)
y=(24-x)*0.1
plt.plot(x,y,color="orange",label="Fitting Curve",linewidth=2) #画拟合曲线

plt.legend()
plt.show()
'''


''' test the ease function for demand '''

plt.figure(figsize=(8,6))
#plt.scatter(HXi,HYi,color="red",label="Real dataset",linewidth=3) #画样本点
#x=np.linspace(1,12,1000)
AX=np.linspace(1,24,1000)
AX=AX/24
c=1
b=0
AY= -c * ( AX*AX*AX*AX*AX*AX- 1) + b   # easeOutQuart
#a*x**6+b*x**5+c*x**4+d*x**3+e*x**2+f*x+g
  # easeOutQuart
#BY=c * ( -math.pow( 2, -10 * AX ) + 1 ) + b  # easeOutExpo

plt.plot(AX,AY,color="orange",label="easeOutQuart for demand function in PeakTime",linewidth=2) #画拟合曲线

font2 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 14,
}
plt.xlabel('scaled price',font2)
plt.ylabel('Scaled numbers of parking user',font2)


'''
x=np.linspace(1,24,1000)
y=(1*a*x**6+1*b*x**5+1*c*x**4+1*d*x**3+1*e*x**2+f*x)/(0.2*x+1)+g+0.25
plt.plot(x,y,color="blue",label="Price",linewidth=2) #画拟合曲线
'''
plt.legend()
plt.show()

plt.figure(figsize=(8,6))
CY= c * ( (1-AX)*(1-AX)*(1-AX)*(1-AX)*(1-AX)*(1-AX)- 1) + b+2
plt.plot(AX,CY,color="red",label="easeOutQuart for demand function in AdjustableTime",linewidth=2) #画拟合曲线

font2 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 14,
}
plt.xlabel('scaled price',font2)
plt.ylabel('Scaled numbers of parking user',font2)


plt.legend()
plt.show()

print (price)
