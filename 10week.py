import numpy as np

#9-1,9-2
arr = np.array([1,2,3,4,5])
print(arr)
print(arr[1])
print(arr[1:4])

#9-3,9-4,9-5
arrr = np.array([[1,2,3],[4,5,6]])
print(arrr)
print(arrr[0,1],arrr[1,2])
print(arrr.shape)

#9-6
arr1 = np.array([1,2,3,4,5,6])
arr2 = arr1.reshape(3,2)
print(arr1)
print(arr2)

#9-7
arr5 = np.array([2,3,4])
result = arr5+2
print(result)

#9-8
arr3 = np.array([2,3,4])
arr4 = np.array([5,6,7])
result = arr3+arr4
print(result)

#9-9
import matplotlib.pyplot as plt

x = np.linspace(-1,1,100)
y = x**2

plt.figure(figsize=(5,3))
plt.plot(x,y,label='y=x^2')
plt.legend()
plt.show()

#9-10,9-11
year = [2006,2009,2012,2015,2018]
kor = [547,546,554,524,526]

plt.figure(figsize=(5,3))
plt.plot(year,kor)
plt.ylim(500,500)
plt.xlabel('year')
plt.ylabel('score')
plt.show()

ind= np.arange(len(year))

plt.xticks(ind,year)

#9-12
nation = ['Korea','USA','Japan','France']
men = [175.5,176.9,172.1,178.6]
women = [163.2,163.3,158.5,164.5]
ind1 = np.arange(len(nation))

plt.bar(ind,men,color='b',label='women')