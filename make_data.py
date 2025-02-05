
import elementpath
from xml.etree import ElementTree
import cv2
import os


dataset_yolo = "C:\Users\PycharmProjects\pythonProject1\dataset"
data = os.listdir("C:\Users\PycharmProjects\pythonProject1\images_fpr_proekt")
jo = 0
for i in data:
  jo += 1
images = data[:jo//2]
labels = data[jo//2:jo]
u = 0
len = 0
for i in labels:
  len += 1
count_train = 0
count_val = 0



for i in labels:

  count_train += 1
  xmax, xmin, ymax, ymin = 0, 0, 0, 0
  tree = ElementTree.parse(data + i)
  root = tree.getroot()

  for child in root[6][4]:
     if child.tag == 'xmax':
        xmax = child.text
     elif child.tag == 'xmin':
        xmin = child.text
     elif child.tag == 'ymax':
        ymax = child.text
     elif child.tag == 'ymin':
        ymin = child.text

  with open("C:\Users\Максим\PycharmProjects\pythonProject1\dataset\train\labels" + str(u) + ".txt", "w") as file:
     file.write(f"{xmax} {ymax} {xmin} {ymin}\n")
  if u + 1 == (labels.index(i) + 1) - (labels.index(i) + 1 // 100 *20):
    break


for i in labels[u:]:

  count_val += 1
  xmax2, xmin2, ymax2, ymin2 = 0, 0, 0, 0
  tree = ElementTree.parse('/content/drive/MyDrive/neyro_sety/proelt/dataset/' + i)
  root = tree.getroot()

  for child in root[6][4]:
     if child.tag == 'xmax':
        xmax2 = child.text
     elif child.tag == 'xmin':
        xmin2 = child.text
     elif child.tag == 'ymax':
        ymax2 = child.text
     elif child.tag == 'ymin':
        ymin2 = child.text

  with open("/content/drive/MyDrive/neyro_sety/proelt/dataset_for_yolo/train/labels/" + str(u) + ".txt", "w") as file:
     file.write(f"{xmax2} {ymax2} {xmin2} {ymin2}\n")
     print(f"{xmax2} {ymax2} {xmin2} {ymin2}\n")


print("val:", count_val)
print("train:", count_train)