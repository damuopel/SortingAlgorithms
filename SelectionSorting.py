import matplotlib.pyplot as plt
import gif
import random

def swap(array,firstIndex,secondIndex):
    array[firstIndex], array[secondIndex] = array[secondIndex], array[firstIndex]
    return array

def indexOfMinimum(array,startIndex):
    minValue = array[startIndex]
    minIndex = startIndex
    
    for i in range(minIndex+1,len(array)):
        if array[i] < minValue:
            minIndex = i
            minValue = array[i]
            
    return minIndex

def selectionSort(array):
    for i in range(0,len(array)):
        frame = plot(array)
        frames.append(frame)
        minIndex = indexOfMinimum(array,i)
        array = swap(array,i,minIndex)
        
    return array

@gif.frame
def plot(array):
    plt.figure()
    plt.bar(list(range(1,len(array)+1)), array, width = 1, color = 'r', edgecolor = 'k')
    plt.axis('off')
      
if __name__ == '__main__':
    n = 50
    array = random.sample(range(0,n),n)
    frames = []
    selectionSort(array)
    gif.save(frames,'Selection.gif',duration=200)
    