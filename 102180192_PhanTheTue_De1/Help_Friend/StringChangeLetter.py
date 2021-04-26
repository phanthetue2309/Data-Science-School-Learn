def StringChallenge(num):
  str1 =''
  num_tmp = str(num)
  # code goes here
  for x in range(len(num_tmp)-1):
    if int(num_tmp[x]) % 2 == 0 and int(num_tmp[x+1]) % 2 == 0:
      if int(num_tmp[x]) == 0 or int(num_tmp[x+1])==0:
        str1 = str1 + num_tmp[x]
      else:
        str1 = str1 + num_tmp[x] + '*'
    elif int(num_tmp[x]) % 2 == 1 and int(num_tmp[x+1]) % 2 == 1:
      str1 = str1 + num_tmp[x] + '-'
    else:
      str1 = str1 + num_tmp[x]

  str1 = str1 + num_tmp[-1]    
  return str1

# keep this function call here 
print(StringChallenge(input()))