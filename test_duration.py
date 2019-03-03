import subprocess
import json

def ffprobe(file):
	meta_json = subprocess.check_output([
		'ffprobe', '-v', 'warning', '-print_format',
		'json', '-show_streams', '-show_format', str(file)],
        universal_newlines=True
	)
	return json.loads(meta_json)

def test_duration():
    fnin = 'video.mp4'
    fnout = 'video_480p.mp4'
    fnout2 = 'video_720p.mp4'
    orig_meta = ffprobe(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])
    meta_480 = ffprobe(fnout)
    duration_480 = float(meta_480['streams'][0]['duration'])
    meta_720 = ffprobe(fnout2)
    duration_720 = float(meta_720['streams'][0]['duration'])

    if orig_duration == duration_480 == duration_720:
        return True
    else:
        return False


if __name__ == '__main__':
    test_duration()