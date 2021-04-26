 
import json
  
# Opening JSON file
f = open('data.json', 'r', encoding='utf-8')
  
# Reading from file
data = json.loads(f.read())
new_data = data[0]['chaperData'] 
f.close()

import csv

def writeToCSV_Overriding() :
    '''
    This function writing to a new file 
    '''
    with open('tiki.csv', mode='w',encoding='utf-8') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['ID', 'Name Product', 'Price (VND) ' , 'Total Review', 'Discount(%)'])
        k = 0 
        for i in new_data : 
            product = i['product'].replace('"','')

            price = i['price'].replace(" ₫","")
            price = price.replace(".","")

            review = i['review'].replace("(","")
            review = review.replace(")","")
            try : 
                review = int(review)
            except :
                review = 0 
            discount = i['discount'].replace("-","")
            discount = discount.replace("%","")

            employee_writer.writerow([k,product,price,review,discount] )
            k += 1

def writeToCSV_Not_Overriding(k) :
    # write not overriding 
    with open('tiki.csv', mode='a',encoding='utf-8') as employee_file: 
        # mode = 'a' mean just write append in existing file 
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         
        for i in new_data : 
            product = i['product'].replace('"','')

            price = i['price'].replace(" ₫","")
            price = price.replace(".","")

            review = i['review'].replace("(","")
            review = review.replace(")","")
            try : 
                review = int(review)
            except :
                review = 0 
            discount = i['discount'].replace("-","")
            discount = discount.replace("%","")

            employee_writer.writerow([k,product,price,review,discount] )
            k += 1

writeToCSV_Overriding()
#writeToCSV_Not_Overriding(48)