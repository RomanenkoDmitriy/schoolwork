#run `pip install pillow` before
#make sure you have `requests` lib installed
#use https://pillow.readthedocs.io/en/stable/handbook/tutorial.html for reference

from PIL import Image
import requests
import os
import threading


URL = 'https://lp-cms-production.imgix.net/2019-06/4871827ef10d74079fb636806d371ccc-brighton-hove.jpg'
URL2 = 'https://vjoy.cc/wp-content/uploads/2020/09/bezymyannyjkvytstsk.jpg'
URL3 = 'https://i.pinimg.com/736x/95/30/41/953041070f000d45c05c912005f63724.jpg'
URL5 = 'https://mirpozitiva.ru/wp-content/uploads/2019/11/1472042719_15.jpg'

def load_image(url, filename='example.jpg'):
    with Image.open(requests.get(url, stream=True).raw) as image:
        image.save(os.path.join(os.getcwd(), filename))



def print_image_data(file):
    image = Image.open(file)
    print(image.size, image.mode)

def is_square_image(file):
    image = Image.open(file)
    return image.size[0] == image.size[1]

def create_thumbnail(file):
    '''# TODO: handle all errors on thumbnail creation'''
    thumbnail_size = (200, 200)
    image = Image.open(file)
    image.thumbnail(thumbnail_size)
    image.save('thumbnail.jpg', 'JPEG')

def is_thumbnail(file):
    thumbnail_size = [200, 200]
    image = Image.open(file)
    return image.size == thumbnail_size

def rotate_image(file, degrees):
    image = Image.open(file)
    rotated = image.rotate(degrees)
    rotated.save('rotated.jpg')

def flip_image(file, direction):
    directions = {'LT': Image.FLIP_LEFT_RIGHT, 'TB': Image.FLIP_TOP_BOTTOM}
    image = Image.open(file)
    out = image.transpose(directions[direction])
    out.save('flipped.jpg')

def copy_images_to_dir(dirname):
    '''Copies all images from current folder into subfolder'''
    path = os.path.join(os.getcwd())
    for file in os.listdir(path):
        try:
            image = Image.open(file)
            image.save(os.path.join(os.getcwd(), dirname, image.filename))
        except:
            break

def delete_images(path=os.path.join(os.getcwd())):
    for file in os.listdir(path):
        if file.endswith('.jpg'):
            os.remove(file)

''' TODO: create a function that will save rectangle area from given image to the separate file'''
# with name 'rectangle.jpg'. Coordinates of rectangle have to be passed as tuple of 4 integers
def rectangular_area(file):
    path = os.path.join(os.getcwd(), 'images', file)
    box = (500, 150, 600, 300)
    with Image.open(path) as image:
        im_crop = image.crop(box)
        im_crop.save('rectangle.jpg', quality=95)




if __name__ == '__main__':
    load_img = threading.Thread(target=load_image, args=(URL, 'img1.jpg'))
    load_img2 = threading.Thread(target=load_image, args=(URL2, 'img2.jpg'))
    load_img3 = threading.Thread(target=load_image, args=(URL3,'img3.jpg'))
    # load_img4 = threading.Thread(target=load_image, args=(URL4, 'img4.jpg'))
    load_img5 = threading.Thread(target=load_image, args=(URL5, 'img5.jpg'))
    load_img.start()
    load_img2.start()
    load_img3.start()
    # load_img4.start()
    load_img5.start()
    # load_image(URL)
    # print_image_data('example.jpg')
    # print(is_square_image('example.jpg'))
    # create_thumbnail('example.jpg')
    # print(is_thumbnail('thumbnail.jpg'))
    # rotate_image('images/example.jpg', 45)
    # flip_image('example.jpg', 'LT')
    # copy_images_to_dir('images')
    # delete_images()
    # rectangular_area('example.jpg')
    print('Done!')
