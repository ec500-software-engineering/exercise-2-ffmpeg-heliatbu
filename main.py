#Copyright 2019 heli@bu.edu by He Li
import os
import subprocess
from threading import Thread
from queue import Queue
import pytest
queue_720 = Queue()
queue_480 = Queue()

def ffmpeg_720():
    while not queue_720.empty():
        filename = queue_720.get()
        file = filename.split('.')
        output_name = file[0] + '_720.mp4'
        cmd = 'ffmpeg -y -i {input} -b:v {bit_rate}M -r {fps} -s hd{res} {output}'
        cmd = cmd.format(input = filename, bit_rate = 30, fps = 60, res= 720, output = output_name)
        subprocess.run(cmd)
        print('Convert ' + filename + ' to 720p successfully.')

def ffmpeg_480():
    while not queue_480.empty():
        filename = queue_480.get()
        file = filename.split('.')
        output_name = file[0] + '_480.mp4'
        cmd = 'ffmpeg -y -i {input} -b:v {bit_rate}M -r {fps} -s hd{res} {output}'
        cmd = cmd.format(input=filename, bit_rate=30, fps=60, res=480, output=output_name)
        subprocess.run(cmd)
        print('Convert ' + filename + ' to 480p successfully.')

if __name__ == '__main__':
    thread1 = Thread(target=ffmpeg_720)
    thread2 = Thread(target=ffmpeg_480)
    for file in os.listdir(os.getcwd()):
        if file.endswith('.mp4'):
            '''
            Limit video number to 1
            '''
            if queue_480.qsize() == 0:
                queue_480.put(file)
            if queue_720.qsize() == 0:
                queue_720.put(file)
            break

    thread1.start()
    thread2.start()