#count number image in a foler and its subfolder, print the number of images in each subforder
import os

def count_image(image_dir1, image_dir2):
    for destination in os.listdir(image_dir1):
        count1 = 0
        for img in os.listdir(os.path.join(image_dir1, destination)):
            count1 += 1
        
        count2 = 0
        if not os.path.exists(os.path.join(image_dir2, destination)):
            count2 = 0
        else:
            for img in os.listdir(os.path.join(image_dir2, destination)):
                count2 += 1

        print(destination, count1, count2)

image_dir1 = "/media/mountHDD2/venus/ChangeWeather/leftImg8bit/test"
image_dir2 = "/media/mountHDD2/venus/ChangeWeather/sunny/test"
count_image(image_dir1, image_dir2)
