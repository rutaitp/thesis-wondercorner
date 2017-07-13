#uses Uberi Speech recognition library: https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py

#! /usr/bin/python
import os
from os import path, listdir
import speech_recognition as sr
import time

path_to_watch = "/var/spool/asterisk/answers/loader/"

before = dict ([(f, None) for f in os.listdir (path_to_watch)])

while 1:
  #run every 10 seconds
  time.sleep (10)

  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  
  #check if there are any new files added and 
  if added:
  	for audioFile in added:
  		#get the full path of each file
  		AUDIO_FILE = os.path.join(os.path.dirname(path_to_watch), audioFile)
  		print AUDIO_FILE

		#use the audio file as the audio source
		r = sr.Recognizer()
		with sr.AudioFile(AUDIO_FILE) as source:
			audio =r.record(source) #read the entire audio file

		# recognize speech using Google Cloud Speech
		GOOGLE_CLOUD_SPEECH_CREDENTIALS = r""""""

		try:
			text_file = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
			print "Google Cloud Speech thinks you said " + text_file
		except sr.UnknownValueError:
			continue
			print "Google Cloud Speech could not understand audio"
		except sr.RequestError as e:
			print "Could not request results from Google Cloud Speech service; {0}".format(e)

		# get the timestamp to later use in file name
		ts = int(time.time())

		#write each text into a new text file
		if (text_file):
			save_path = "/CODE/answers_text/"

			name_of_file = str(ts) + ".txt"

			completeName = os.path.join(save_path, name_of_file)

			file_text = open(completeName, "w")
			file_text.write(text_file)
			file_text.close()

  if removed:
  		for j in removed:
  			print j

  before = after