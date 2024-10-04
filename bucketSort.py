 def bucketSort(arr):
     counts = [0] * 5

     for num in arr:
         counts[num] += 1
     
     for num in range(len(counts)):
         for _ in range(counts[num]):
             arr[i] = num 
             i += 1
     return arr

