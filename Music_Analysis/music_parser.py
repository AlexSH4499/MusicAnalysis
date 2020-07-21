# Beat tracking example
from flask import Flask, jsonify, request
from flask_cors import CORS

from Music_DB.handler.musichandler import MusicHandler

from __future__ import print_function
import librosa

# file accessor tests
app = Flask(__name__)
CORS(app)

filen = r"C:\git\MusicAnalysis\Music_Analysis\"
filen.append(MusicHandler().getMusicbyId(1))

# 1. Get the file path to the included audio example
filename = r"C:\git\MusicAnalysis\Music_Analysis\Megaman_ZX_-_Green_Grass_Gradiation_NITRO_Remix (1).wav"

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# python -c "import numpy; print(numpy.version.version)" ; to change switch modules from numpy to whatever needed
# pip install funcsigs==version.version.version ; to switch, change version to a number
# intended output: 136.00 beats per minute using wav included
