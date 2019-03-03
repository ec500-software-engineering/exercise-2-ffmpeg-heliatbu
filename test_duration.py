import subprocess
import json
from pathlib import Path
from pytest import approx

def ffprobe(filein: Path) -> dict:
	meta_json = subprocess.check_output([
		'ffprobe', '-v', 'warning', '-print_format',
		'json', '-show_streams', '-show_format', filein],
		universal_newlines=True
	)
	return json.loads(meta_json)

def test_duration():
    fnin = 'video.mp4'
    fnout = 'video_480.mp4'
    fnout2 = 'video_720.mp4'
    orig_meta = ffprobe(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])
    meta_480 = ffprobe(fnout)
    duration_480 = float(meta_480['streams'][0]['duration'])
    meta_720 = ffprobe(fnout2)
    duration_720 = float(meta_720['streams'][0]['duration'])
    assert orig_duration == approx(duration_480) == approx(duration_720)
