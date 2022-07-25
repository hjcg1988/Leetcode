from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  count=0
  seats={}
  #i will create a dictionary to mark the used places and not usable seats
  for i in S:
      seats[i]=2
      if N >= 1:
        for x in range(1,K+1):
            seats[i-x]=1
            seats[i+x]=1
  #iterate over the dictionary to check if seats are free
  for val in range(1,N+1):
    #check if val is not in dictionary to see if it is an open space
    if val not in seats:
        #if it is an open space check if the seats on the side are enough for security guidelines
        for x in range(1,K+1):
          if seats.get(val-x) == 2 or seats.get(val+x) == 2 :
            break
        #it this point is reached the seat is valid and complies with the guidelines so we set the value in the dictionary
        seats[val]=2
        #we use range over the value of K to set the side seats equal to 1 in the dictionary to avoid processing them as open
        for x in range(1,K+1):
          seats[val+x]=1
          seats[val-x]=1
        #we increase the count 1 as we found a valid open seat
        count += 1
        
      
  return count
