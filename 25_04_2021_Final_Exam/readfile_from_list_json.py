 
import csv
import json
import os  

def writeToCSV_Overriding() :
    '''
    This function writing to a new file 
    '''
    with open('full_tiki.csv', mode='w',encoding='utf-8') as employee_file:
        writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Name','Category','List-Price','Price','Total Review', 
                            'Rating Average','Discount','Discount Rate'])
     
def writeToCSV_Not_Overriding(new_data) :
    '''
    This function writes not overriding. This write append file 
    mode = 'a' mean just write append in existing file 
    '''
    with open('full_tiki.csv', mode='a',encoding='utf-8') as employee_file: 
        writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         
        for i in new_data : 
            name = i['name'].replace('"','')
            category = i['category']
            list_price = i['list_price']
            price = i['price']
            review = i['review_count']
            rating = i['rating_average']
            discount = i['discount']
            discount_rate = i['discount_rate']
            writer.writerow([name,category,list_price,price,review,rating,discount,discount_rate] )


# Opening JSON file and write file 
writeToCSV_Overriding() # write file first 
readfile = [f for f in os.listdir('data/') if f.endswith('.json')] # get name of all files
for file_data in readfile:
    read_data = open('data' +'/'+ file_data , 'r', encoding='utf-8')
    data = json.load(read_data)
    writeToCSV_Not_Overriding(data)
    read_data.close()