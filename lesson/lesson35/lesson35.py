# декоратор засецения времени
# функция лоад имеджб ротейт. копи шмдж
# создать функцию которая записует 10т строк в тхт файл
#  для всех функций создать функцию которые создадут 3 потока
#  создать функцию 3 процеса
# функция которая вызывает все процесы
# все задекорировать


import time
from PIL import Image
import requests
import os
import threading
from multiprocessing import Process

URL = 'https://klike.net/uploads/posts/2019-05/1556708032_1.jpg'
URL1 = 'https://bipbap.ru/wp-content/uploads/2017/05/1_small-4.jpg'
URL2 = 'https://vypechka-online.ru/wp-content/uploads/2019/09/EQgJ4p77Aeo.jpg'


def time_decor(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        print(f'{func.__name__} {args} {time.time() - start_time}')
        return func(*args)
    return wrapper


def load_image(url='https://klike.net/uploads/posts/2019-05/1556708032_1.jpg', filename='example.jpg'):
    with Image.open(requests.get(url, stream=True).raw) as image:
        image.save(os.path.join(os.getcwd(), filename))


def rotate_image(file, name_file, degrees):
    image = Image.open(file)
    rotated = image.rotate(degrees)
    rotated.save(name_file)


def copy_images_to_dir(dirname):
    path = os.path.join(os.getcwd())
    for file in os.listdir(path):
        try:
            image = Image.open(file)
            image.save(os.path.join(os.getcwd(), dirname, image.filename))
        except:
            break

def write_str(string, name_file):
    path = os.path.join(os.getcwd(), name_file)
    with open(path, 'a') as file:
        for i in range(10000):
            file.write(string)


def delete_images(name, path=os.path.join(os.getcwd())):
    for file in os.listdir(path):
        if file == name:
            os.remove(file)


@time_decor
def treid_load_image(func):
    treid = threading.Thread(target=func, args=(URL, 'img.jpg'))
    treid2 = threading.Thread(target=func, args=(URL1, 'img2.jpg'))
    treid3 = threading.Thread(target=func, args=(URL2, 'img3.jpg'))
    treid.start()
    treid2.start()
    treid3.start()


@time_decor
def treid_rotate_image(func):
    treid = threading.Thread(target=func, args=('img.jpg', 'rotate_img.jpg',  45))
    treid2 = threading.Thread(target=func, args=('img2.jpg', 'rotate_img2.jpg',  90))
    treid3 = threading.Thread(target=func, args=('img3.jpg', 'rotate_img3.jpg',  180))
    treid.start()
    treid2.start()
    treid3.start()


@time_decor
def treid_copy_images_to_dir(func, dirname):
    treid = threading.Thread(target=func, args=(dirname,))
    treid2 = threading.Thread(target=func, args=(dirname,))
    treid3 = threading.Thread(target=func, args=(dirname,))
    treid.start()
    treid2.start()
    treid3.start()



@time_decor
def treid_write_str(func, string, name_file):
    treid = threading.Thread(target=func, args=(string, f'{name_file}.txt'))
    treid2 = threading.Thread(target=func, args=(string, f'{name_file}2.txt'))
    treid3 = threading.Thread(target=func, args=(string, f'{name_file}3.txt'))
    treid.start()
    treid2.start()
    treid3.start()

@time_decor
def treid_delete_images(func):
    treid = threading.Thread(target=func, args=('img.jpg', os.path.join(os.getcwd(), 'images')))
    treid2 = threading.Thread(target=func, args=('img2.jpg', os.path.join(os.getcwd(), 'images')))
    treid3 = threading.Thread(target=func, args=('img3.jpg', os.path.join(os.getcwd(), 'images')))
    treid.start()
    treid2.start()
    treid3.start()


@time_decor
def proc_load_image(func):
    proc = Process(target=func, args=(URL, 'img.jpg'))
    proc2 = Process(target=func, args=(URL1, 'img2.jpg'))
    proc3 = Process(target=func, args=(URL2, 'img3.jpg'))
    proc.start()
    proc.join()

    proc2.start()
    proc2.join()

    proc3.start()
    proc3.join()


@time_decor
def proc_rotate_image(func):
    proc = Process(target=func, args=('rotate_img.jpg', 45))
    proc2 = Process(target=func, args=('rotate_img2.jpg', 90))
    proc3 = Process(target=func, args=('rotate_img3.jpg', 180))
    proc.start()
    proc.join()

    proc2.start()
    proc2.join()

    proc3.start()
    proc3.join()


@time_decor
def proc_copy_images_to_dir(func, dirname):
    proc = Process(target=func, args=(dirname,))
    proc2 = Process(target=func, args=(dirname,))
    proc3 = Process(target=func, args=(dirname,))
    proc.start()
    proc.join()

    proc2.start()
    proc2.join()

    proc3.start()
    proc3.join()


@time_decor
def proc_write_str(func, string, name_file):
    proc = Process(target=func, args=(string, f'{name_file}.txt'))
    proc2 = Process(target=func, args=(string, f'{name_file}2.txt'))
    proc3 = Process(target=func, args=(string, f'{name_file}3.txt'))
    proc.start()
    proc.join()

    proc2.start()
    proc2.join()

    proc3.start()
    proc3.join()


@time_decor
def proc_delete_images(func):
    proc = Process(target=func, args=('img.jpg', os.path.join(os.getcwd(), 'images')))
    proc2 = Process(target=func, args=('img2.jpg', os.path.join(os.getcwd(), 'images')))
    proc3 = Process(target=func, args=('img3.jpg', os.path.join(os.getcwd(), 'images')))
    proc.start()
    proc.join()

    proc2.start()
    proc2.join()

    proc3.start()
    proc3.join()



@time_decor
def defolt_func(func, *args):
    func(args)
    func(args)
    func(args)


if __name__ == '__main__':
    treid_load_image(load_image)
    treid_rotate_image(rotate_image)
    treid_copy_images_to_dir(copy_images_to_dir, 'images')
    treid_write_str(write_str, 'some string', 'test_text')
    treid_delete_images(delete_images)

    proc_load_image(load_image)
    proc_rotate_image(rotate_image)
    proc_copy_images_to_dir(copy_images_to_dir, 'images')
    proc_write_str(write_str, 'some string', 'test_text')
    proc_delete_images(delete_images)

    defolt_func(load_image)
    defolt_func(rotate_image)
    defolt_func(copy_images_to_dir, 'images')
    defolt_func(write_str, 'some string', 'test_text')
    defolt_func(delete_images)

