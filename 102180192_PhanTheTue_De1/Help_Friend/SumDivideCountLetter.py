def SearchingChallenge(strParam):
  sum_num = 0
  count_letters = 0
  # code goes here
  for x in range(len(strParam)):
    if strParam[x].isnumeric():
      sum_num += int(strParam[x])
    elif strParam[x].isalpha():
      count_letters += 1
    else:
      continue

  
  return round(sum_num/count_letters)

# keep this function call here 
print(SearchingChallenge(input()))