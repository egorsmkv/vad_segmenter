from os.path import dirname

import librosa
import webrtcvad

from tools import read_wave, frame_generator, vad_collector, write_wave

source = dirname(__file__) + '/raw_data/1.wav'
input_file_sample_rate = 48000
output_file_sample_rate = 16000

audio, sample_rate = read_wave(source)
vad = webrtcvad.Vad(3)

time = 30
frames = frame_generator(time, audio, sample_rate)
frames = list(frames)

wave, _ = librosa.load(source, sr=input_file_sample_rate)
segments = vad_collector(wave, sample_rate, time, 300, vad, frames)

for i, segment in enumerate(segments):
    filename = dirname(__file__) + f'/segments/{i}.wav'
    write_wave(filename, segment, output_file_sample_rate)

    print(f'Saved: {filename}')
