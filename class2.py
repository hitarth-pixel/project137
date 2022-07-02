import csv
final_rows1=[]

with open("final.csv") as f:
  csvreader=csv.reader(f)
  for row in csvreader:
    final_rows1.append(row)
final_list1=[]

for star_data in final_rows1:
  temp_dict={
    "name":star_data[1],
    "distance_from_earth":star_data[2],
    "star_mass":star_data[3],
    "star_radius":star_data[4],
    "gravity":star_data[5],
  }
  final_list1.append(temp_dict)
data1=final_list1

final_rows2=[]
with open("final2.csv") as f:
  csvreader=csv.reader(f)
  for row in csvreader:
    final_rows1.append(row)
final_list2=[]
for star_data in final_rows2:
  temp_dict={
    "name":star_data[1],
    "distance_from_earth":star_data[2],
    "star_mass":star_data[3],
    "star_radius":star_data[4],
    "gravity":star_data[5]
  }
  #temp_dict["specifications"]=final_rows2[star_data[1]]
  final_list2.append(temp_dict)
data2=final_list2