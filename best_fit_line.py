from statistics  import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.linear_model import LinearRegression
import random

style.use('fivethirtyeight')

# xs=np.array([1,2,3,4,5,6,7,8,9,10],dtype=np.float64)
x=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]],dtype=np.float64)
# ys=np.array([4,5,3,5,6,7,3,8,6,11],dtype=np.float64)

def create_dataset(hm,varience,step=2,correlation=True):
    val=1
    ys=[]
    for i in range(hm):
        y=val+random.randrange(-varience,varience)
        ys.append(y)
        if correlation and correlation==True:
            val+=step
        elif correlation and correlation==False:
            val-=step
    xs=[i for i in range(hm)]
    return np.array(xs,dtype=np.float64),np.array(ys,np.float64)

def best_fit_line(xs,ys):
    numerator=mean(xs)*mean(ys)-mean(xs*ys)
    denominator=mean(xs)**2-mean(xs**2)
    m=numerator/denominator
    b=mean(ys)-m*mean(xs)
    return m,b

def squared_error(ys_orig, ys_line):
    return sum((ys_line-ys_orig)**2)

def coef_of_determination(ys_orig,ys_line):
    ys_mean_line=[(mean(ys_orig)) for y in ys_orig]
    squared_error_of_regression_line=squared_error(ys_orig, ys_line)
    squared_error_of_mean_line = squared_error(ys_orig, ys_mean_line)
    return 1-(squared_error_of_regression_line/squared_error_of_mean_line)

xs,ys=create_dataset(40,2,2,True)
print("xs=%s & ys=%s"%(xs,ys))

m,b=best_fit_line(xs,ys)
regression_line = [(m*x)+b for x in xs]

r_square=coef_of_determination(ys,regression_line)
print("r square=",r_square)

predict_x = 5
predict_y = m*predict_x+b
print("slop=%s & intercept=%s"%(m,b))

plt.scatter(xs,ys)
# plt.plot(xs,ys)
plt.scatter(predict_x,predict_y,s=100,color='g')
plt.plot(xs,regression_line)
plt.show()
