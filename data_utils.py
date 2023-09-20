import os
import librosa
import numpy as np 

def mlp_data_preprocess(AI_music_dir, real_music_dir):
  folderName = AI_music_dir
  X_list = []
  y_list = []
  MAX_SONG_LENGTH = 769
  for filename in os.listdir(folderName):

    y,sr = librosa.load(folderName + filename)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    truncated_mfcc = mfcc[:, :MAX_SONG_LENGTH]


    mfcc_flattened = np.ravel(truncated_mfcc)
    X_list.append(mfcc_flattened)
    y_list.append(1)

  folderName = real_music_dir

  MAX_SONG_LENGTH = 769
  for filename in os.listdir(folderName):

    y,sr = librosa.load(folderName + filename)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    truncated_mfcc = mfcc[:, :MAX_SONG_LENGTH]


    mfcc_flattened = np.ravel(truncated_mfcc)
    X_list.append(mfcc_flattened)
    y_list.append(0)

  return X_list, y_list



  

def lstm_data_preprocess(AI_music_dir, real_music_dir):
  folderName = AI_music_dir
  X_list = []
  y_list = []
  MAX_SONG_LENGTH = 769
  for filename in os.listdir(folderName):

    y,sr = librosa.load(folderName + filename)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    truncated_mfcc = mfcc[:, :MAX_SONG_LENGTH]


    
    X_list.append(truncated_mfcc)
    y_list.append(1)

  folderName = real_music_dir

  MAX_SONG_LENGTH = 769
  for filename in os.listdir(folderName):

    y,sr = librosa.load(folderName + filename)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    truncated_mfcc = mfcc[:, :MAX_SONG_LENGTH]


    X_list.append(truncated_mfcc)
    y_list.append(0)
    
  return X_list, y_list
