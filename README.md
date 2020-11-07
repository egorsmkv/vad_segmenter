# VAD Segmeter

This is a tool to segment WAV files using WebRTC's Voice Activity Detector (VAD)

## How to use

### Install dependencies

```
pipenv install
pipenv shell
```

### Run

```
python segmenter.py
```

Edit the `segmenter.py` file to config parameters (sample rate and an input file).

All segmented files will appear in the `segments` folder as WAV files.
