# Multithreading
# import threading
# import time
#
#
# def func_n():
#     for number in range(10):
#         print(f'NUMBER => {number}')
#         time.sleep(1)
#
#
# def func_a():
#     for alphabet in 'ABCDEFGHIJ':
#         print(f'Character => {alphabet}')
#         time.sleep(1)
#
#
# def func_w():
#     for word in 'Hello teacher':
#         print(f'Word => {word}')
#         time.sleep(1)
#
#
# thread1 = threading.Thread(target=func_n)
# thread2 = threading.Thread(target=func_a)
# thread3 = threading.Thread(target=func_w)
#
# start_time = time.time()
# thread1.start()
#
# thread2.start()
#
# thread3.start()
#
# thread1.join()
# thread2.join()
# thread3.join()
# end_time = time.time()
# #print(f'Total time => {end_time - start_time}')
# #print('Process finished')
#
#
# def say_full_name(full_name):
#     print(f'Hello my full_name {full_name}')
#     time.sleep(1)
#
#
# def func(m):
#     for square in range(1, m):
#         print(square ** 2)
#         time.sleep(1)
#
#
# func1 = threading.Thread(target=say_full_name, args=('Hamidova Nozimabonu',))
# func2 = threading.Thread(target=func, args=(20,))
#
# func1.start()
# func2.start()
#
# func1.join()
# func2.join()


import pyttsx3
engine = pyttsx3.init()

engine.say("Hello N42 Guys")
engine.setProperty('rate', 155)
rate = engine.getProperty('rate')
print(rate)
engine.save_to_file('Hello Guys','n42.mp3')
engine.runAndWait()
engine.stop()



engine.say('Hello my name is Nozimabonu, my last name is Hamidova. I am 17 years old')
engine.setProperty('rate', 125)
rate = engine.getProperty('rate')
print(rate)
engine.save_to_file('About me', 'n42.mp3')
engine.runAndWait()
engine.stop()


# def speak(text):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)
#     engine.say('This is function number of square')
#     engine.runAndWait()
