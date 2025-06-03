from PIL import Image
import csv

img = Image.open('../images/original.png')

with open('../../data/trees.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x','y']) 