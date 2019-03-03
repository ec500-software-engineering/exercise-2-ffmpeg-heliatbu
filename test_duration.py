import subprocess
import json
from pathlib import Path
from pytest import approx

def ffprobe(file: Path) -> dict:
    meta_json = subprocess.check_output([
		'ffprobe', '-v', 'warning', '-print_format',
		'json', '-show_streams', '-show_format', file],
    universal_newlines = True
	)
    return json.loads(meta_json)

def test_duration():
    fOri = 'video.mp4'
    f480 = 'video_480p.mp4'
    f720 = 'video_720p.mp4'
    orig_meta = ffprobe(fOri)
    meta_480 = ffprobe(f480)
    meta_720 = ffprobe(f720)
    video_duration = float(orig_meta['streams'][0]['duration'])
    video_480_duration = float(meta_480['streams'][0]['duration'])
    video_720_duration = float(meta_720['streams'][0]['duration'])
    assert video_duration == approx(video_480_duration) == approx(video_720_duration)

