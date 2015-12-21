# -*- coding:utf-8 -*-
import pyaudio

HMM = '/usr/share/pocketsphinx/model/hmm/fr_FR/'
DIC = '/usr/share/pocketsphinx/model/lm/fr_FR/frenchWords62K.dic'
LM= '/usr/share/pocketsphinx/model/lm/fr_FR/french3g62K.lm.dmp'

TMPFILE = 'tmp.wav'

CHUNK = 512
FORMAT = pyaudio.paALSA
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 2

DETECTS = {
    'cité': 'quitter',
    'cités': 'quitter',
    'quitter': 'quitter',
    'quitté': 'quitter',
    'qui était': 'quitter',
    'fichier': 'fichier',
    'fichiers': 'fichier',
    'bonjour': 'bonjour',
}

COMMANDS = {
    'bonjour': {
        'audio': ['yes1', 'yes2', 'yes3', 'yes4'],
    },
    'fichier': {
        'audio': ['execute1', 'execute2', 'execute3'],
        'cmd': 'ls'
    },
    'quitter': {
        'audio': ['execute1', 'execute2', 'execute3'],
        'python': 'exit(0)'
    },
}
