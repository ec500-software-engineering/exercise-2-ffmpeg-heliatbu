import shutil
import subprocess
import threading
import sys


CMD = 'ffmpeg -y -i {input} -b:v {bit_rate}M -r {fps} -s hd{res} {output}'


def check_ffmpeg():
    FFMPEG = shutil.which('ffmpeg')
    if not FFMPEG:
        raise FileNotFoundError('FFMPEG not found')


def test_func():
    main("video.mp4")


def ffmpeg(name, res):
    output_name = str(res)+"output.mp4"
    cmd = reformat(name, res, output_name)
    subprocess.run(cmd)


def reformat(name, res, output_name):
    cmd = CMD.format(input=name,
                     bit_rate=30,
                     fps=60,
                     res=res,
                     output=output_name)
    return cmd


def main(args):
    check_ffmpeg()
    if args:
        input_name = args
    elif len(sys.argv) != 2:
        raise FileNotFoundError('You did not enter the file name')
    else:
        input_name = sys.argv[1]
    ffmpeg480 = threading.Thread(target=ffmpeg, args=(input_name, 480))
    ffmpeg720 = threading.Thread(target=ffmpeg, args=(input_name, 720))
    ffmpeg480.start()
    ffmpeg720.start()
    print("Start transcoding to 480P and 720P videos.")
    ffmpeg480.join()
    ffmpeg720.join()
    print("All jobs done.")


if __name__ == "__main__":
    main("video.mp4")