from PIL import Image
import csv

img = Image.open('../images/extract_cloud.png')

with open('../../data/cloud.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'y']) 