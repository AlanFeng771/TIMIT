import librosa
import soundfile as sf
import os
import scipy.io.wavfile as wav
file_dir = r'timit\data\lisa\data\timit\raw\TIMIT\TRAIN'
DR_list = os.listdir(file_dir)
wav_list = []
for DR in DR_list:
    chara_dir = os.listdir(f'{file_dir}\{DR}')
    for c in chara_dir:
        file = os.listdir(f'{file_dir}\{DR}\{c}')
        for f in file:
            if f.find('WAV') >= 0:
                wav_list.append(f'{file_dir}\{DR}\{c}\{f}')

            
for wav in wav_list:
    x, fs = librosa.load(wav, sr=None)
    sf.write(wav, x, fs, subtype='PCM_24')
    print(f'{wav} down')

