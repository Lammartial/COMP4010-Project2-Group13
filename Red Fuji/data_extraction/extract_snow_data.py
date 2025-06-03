from PIL import Image
import csv

img = Image.open('../images/extract_snow.png')

with open('../../data/snow.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x','y']) 