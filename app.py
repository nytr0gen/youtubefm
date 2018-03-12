import subprocess
import sys

if len(sys.argv) < 2:
    sys.exit('Usage: python %s youtube-link' % sys.argv[0])

link = sys.argv[1]
yt_cmd = ['youtube-dl',
    '--verbose',
    '--no-color',
    '--newline',
    '--format=(mp3/m4a/bestaudio/best)[height<=?720]',
    '--extract-audio',
    '--audio-format=m4a',
    '--simulate',
    '-g',
    link]
output = subprocess.check_output(yt_cmd)

audio_streams = [v for v in output.decode('utf-8').split('\n') if v != '']
vlc_cmd = ['vlc'] + audio_streams
process = subprocess.Popen(vlc_cmd, stdout=subprocess.PIPE)
