import subprocess
from threading import Thread
from queue import Queue

queue_720 = Queue()
queue_480 = Queue()

def ffmpeg_720():
    try:
        file = queue_720.get()
        filename = file.split('.')
        output_name = filename[0] + '_720p.mp4'
        cmd = 'ffmpeg -i {input} -b:v {bit_rate}M -r {fps} -s hd{res} {output}'
        cmd = cmd.format(input=file, bit_rate=2, fps=30, res=720, output=output_name)
        subprocess.run(cmd)
        print('Convert ' + file + ' to 720p successfully.')
    except Exception:
        print(Exception)

def ffmpeg_480():
    try:
        file = queue_480.get()
        filename = file.split('.')
        output_name = filename[0] + '_480p.mp4'
        cmd = 'ffmpeg -i {input} -b:v {bit_rate}M -r {fps} -s hd{res} {output}'
        cmd = cmd.format(input=file, bit_rate=2, fps=30, res=480, output=output_name)
        subprocess.run(cmd)
        print('Convert ' + file + ' to 480p successfully.')
    except Exception:
        print(Exception)

def main():
    thread1 = Thread(target=ffmpeg_720)
    thread2 = Thread(target=ffmpeg_480)
    try:
        queue_480.put("video.mp4")
        queue_720.put("video.mp4")
    except Exception:
        print(Exception)
    thread1.start()
    thread2.start()
    print("finished.")

if __name__ == '__main__':
    main()