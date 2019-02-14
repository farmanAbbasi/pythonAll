#using numpy
import numpy,math

X=[3,4,5]
Y=[4,5,6]
dotProduct=numpy.dot(X,Y)
print("dot product" ,dotProduct)

#using normal zipping concept
class DP:
     def magnitude(self,X):
         mag=math.sqrt(sum(x**2 for x in X))
         return mag
     def normalised(self):
         magger=self.magnitude(Y)
        

obj1=DP()
print(obj1.normalised())
        

#finding magnitude of a vector
