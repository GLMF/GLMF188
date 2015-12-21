# -*- coding:utf-8 -*-
#!/usr/bin/python

import os
import pyaudio
import wave
import pocketsphinx as ps
import random
import config
import time

def decodeSpeech(hmmd, lmdir, dictp, wavfile, detects, commands): 
    speechRec = ps.Decoder(hmm = hmmd, lm = lmdir, dict = dictp)
    wavFile = file(wavfile,'rb')
    wavFile.seek(44)
    speechRec.decode_raw(wavFile)
    result = speechRec.get_hyp()
    print(result[0])
    if result[0] in detects:
        order = detects[result[0]]
        if 'audio' in commands[order]:
            cmd = 'aplay audio/{}.wav'.format(commands[order]['audio'][random.randint(0, len(commands[order]['audio']) - 1)])
            os.system(cmd)
        if 'cmd' in commands[order]:
            cmd = commands[order]['cmd']
            os.system(cmd)
        if 'python' in commands[order]:
            eval(commands[order]['python'])
 
if __name__ == '__main__':
    while True:
        p = pyaudio.PyAudio()
        stream = p.open(format=config.FORMAT, channels=config.CHANNELS, rate=config.RATE, input=True, frames_per_buffer=config.CHUNK)
        print('En écoute....')
        frames = []
        print str(config.RATE / config.CHUNK * config.RECORD_SECONDS) + " size\n"
        for i in range(0, int(config.RATE / config.CHUNK * config.RECORD_SECONDS)):
            data = stream.read(config.CHUNK)
            frames.append(data)
        os.system('aplay audio/ok.wav')
        stream.stop_stream()
        stream.close()

        fic = wave.open(config.TMPFILE, 'wb')
        fic.setnchannels(config.CHANNELS)
        fic.setsampwidth(p.get_sample_size(config.FORMAT))
        p.terminate()
        fic.setframerate(config.RATE)
        fic.writeframes(b''.join(frames))
        fic.close()

        decodeSpeech(config.HMM, config.LM, config.DIC, config.TMPFILE, config.DETECTS, config.COMMANDS)
