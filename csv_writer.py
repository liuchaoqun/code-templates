import csv
OUT = open('logs/temp.csv', 'a', newline='')
writer = csv.writer(OUT)

writer.writerow([1,2,3,4])
OUT.close()
