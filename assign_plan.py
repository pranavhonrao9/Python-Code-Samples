
import csv




#Read Input1 : DATA

f = open('/Users/pranavhonrao/Desktop/pla_pro/input1.csv')
csv_f = csv.reader(f)

input1_list=[]
input1_dict={}

for row in csv_f:
      input1_list.append(row)
for i in input1_list:
    input1_dict[(i[0])]=int(i[1])



#Read Input2 :TAX

f1 = open('/Users/pranavhonrao/Desktop/pla_pro/input2.csv')
csv_f1 = csv.reader(f1)

input2_list=[]
input2_dict={}

for row1 in csv_f1:
      input2_list.append(row1)


for j in input2_list:
   input2_dict[j[0]]=float(j[1])


#READ Input3: Content


f2 = open('/Users/pranavhonrao/Desktop/pla_pro/input3.csv')
csv_f2 = csv.reader(f2)

input3_list=[]
input3_dict={}

for row2 in csv_f2:
      input3_list.append(row2)


for k in input3_list:
   input3_dict[k[0]]=float(k[1])


quantity_value= { k: round((input1_dict.get(k, 0) * input3_dict.get(k, 0)),2) for k in (set(input1_dict)) }


#Without_tax_values
total_with_out_tax = input3_dict.values()


#Merge with Taxes and entites

tax_dict = { k: round((input2_dict.get(k, 0) * quantity_value.get(k, 0)),2) for k in (set(input2_dict)) }


#print total_with_out_tax
temp=0

for i in total_with_out_tax:
    temp+=i

#print temp

without_tax =  [ v for v in quantity_value.values() ]
#print without_tax



#final value
dict3 = { k: [ tax_dict[k], quantity_value[k] ] for k in quantity_value}




for value in dict3.values():
    if value[0] == value[1]:
         del value[1:]

#print dict3


#value_with_tax
value_with_tax={key: round(sum(values),2) for key, values in dict3.items()}


final_value=0
for value in dict3.values():
    final_value+=sum(value)


actual_tax=final_value-temp


#final_display
for key,value in value_with_tax.iteritems():
    print key,value




print "sales_tax" ,actual_tax
print "final_value",final_value
