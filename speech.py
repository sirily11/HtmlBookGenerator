from __future__ import print_function
import pyaudio
import tempfile
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud.websocket import RecognizeCallback
import json
from Srt_generator import SRT
from tqdm import tqdm
import time
import ffmpeg
import os

def voice_to_text(filename):
    stream = ffmpeg.input(filename)
    stream = ffmpeg.hflip(stream)
    stream = ffmpeg.output(stream, 'temp.wav')
    ffmpeg.run(stream)

    speech_to_text = SpeechToTextV1(
        username='12cbc606-e6bb-4129-ae66-dfe32811972c',
        password='OOTCpkDIyzFI',
        url='https://stream.watsonplatform.net/speech-to-text/api')

    print("Starting voice transfer")
    with open("temp.wav", 'rb') as audio:
        result = speech_to_text.recognize(
            audio=audio,
            content_type='audio/wav',
            timestamps=True,
            word_confidence=True,
            model="zh-CN_BroadbandModel")
        with open('temp.json', 'wb') as f:
            print("Finished")
            f.write(json.dumps(result, ensure_ascii=False).encode("utf8"))


def write_srt(filename):
    with open("temp.json", 'rb') as f:
        jsonfile = json.loads(f.read().decode('utf-8'))
        results = jsonfile['results']
        sentences = []
        time = []
        print("Start parsing json")
        for r in tqdm(results):
            line = r['alternatives'][0]
            starttime = line['timestamps'][0][1]
            endtime = line['timestamps'][len(line['timestamps']) - 1][2]
            time.append({"starttime": starttime, "endtime": endtime})
            sentences.append(line['transcript'].replace(" ", ""))
        print("Finished parsing parsing json")
        srt = SRT(sentences, time)
        with open(filename, 'wb') as f2:
            f2.write(srt.to_srt().encode("utf8"))


# input_filename = input("What is the input file name, ex: *.mp4 ")
start = time.time()
voice_to_text("")

duration = time.time() - start

output_filename = input("What is the output file name, ex: *.srt")
start = time.time()
write_srt(output_filename)
duration += time.time() - start
input("Total time: {}, Press any key to finished".format(duration))
