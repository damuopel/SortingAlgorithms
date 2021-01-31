import matplotlib.pyplot as plt
import gif
import random

def insert(array,rightIndex,value):
    i = rightIndex
    while i >= 0 and array[i] > value:
        array[i+1] = array[i]
        i-=1
    array[i+1] = value
    
def insertionSort(array):
    for i in range(1,len(array)):
        frame = plot(array)
        frames.append(frame)
        insert(array,i-1,array[i])

@gif.frame
def plot(array):
    plt.figure()
    plt.bar(list(range(1,len(array)+1)), array, width = 1, color = 'r', edgecolor = 'k')
    plt.axis('off')
    
if __name__ == '__main__':
    n = 50
    array = random.sample(range(0,n),n)
    frames = []
    insertionSort(array)
    gif.save(frames,'Insertion.gif',duration=200)