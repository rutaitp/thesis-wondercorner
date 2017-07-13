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
		GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{"type": "service_account","project_id": "thesis-165116",
			  "private_key_id": "0517c5bade08ffd158cf18f52d154a5b41f4d79c",
			  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC4cmZTgGoj8OP/\nb7VTx1h96cFm4E2U+xrRItIGMoGnuhE1mM/I2FaOq8ioIGYhmctdb9sR9ygH/Yqu\nqKCVBqkoUdgC7zVwnjfZwIWGnzKhSqxGHdcwACVznBzXyfOv9q2+gq+FcBtgGXLy\ny3PRUE4EITVb9jThotrqQnDg+RIf8XLwFJbFH6cCYkeBRhbRROwRD00bzrB10c13\nBo1kXjSbHdbJWXIe1j9JzpZJTzvZY4PhXcUHizlExTvNYYmD7kdfsq6LYAT06pe2\noNgMQ2QFH4RdivCbAnuZRzLAx9iThKyHek3/468e7qdlI1x8L/iQ0P40nubN2kYG\nrFTSG9iXAgMBAAECggEAXIJUPDE+CwS49darVXe4NH7XV6fMgZpn2tjiCeWvDdbO\n5tjb7lpDH4+dNmX5k4S1cQm3EI2r8EYEFpHQ6K3MjcJu2xnq7a8NSBO9ZMXX+Pmg\n6hHxacvI/PEhrkFGDc1lWxXkvsJ5mHtrIcdVMXhbiMq3HoagA0NRFQl53/xMUORI\nt/RbJ1V7EEUQV2NqG1Dt+EYG0HmqIwdOvBOn35CBDDKReedhPhw0lP81Bqk9VCga\nE+1A7aQg1wZ1yFfcGWGap+/RU/S5vX5aIp5aDxymrW6VtILXpwu1aWMvOzn31fRq\n8Z8xQbJ4ulGREWIzPCGyd4BH/cku+8tqh5qOSxNwAQKBgQDfgldnUMi6JRJmddZR\nzHaTuwTAgCvSI1yCeYtf39uuTYX+gNfs9XwnKUOi0EuoNffZ0Sg3yp8KEP8cwV81\nLera1EzL4CQjJJbjv4F9FYI9+PcrGtmGaj0ly30+HCG2pTbyJo6COdjPhVeF43iL\nhXP1S79Pq14Wx0pbXMaKveAUlwKBgQDTQmWTDZeIlbisUI0ulzeZ42XpoIIHRHGS\nbcjnrbjtucZn1Su3PnZgNLNPRCEwD/pL7yk5WfrqgDabyv7aONdDqOVugEIFh22c\nEDpgE8Ce47IRPeQlb8hmclWkGAPNKgGlNbX063mWhj31ypoo/+rUw7tAbN0V9OE1\nPG7ZEQbcAQKBgBx5QWNDEl9Ma7yr1GLVVmHZmHBho7OAl79zdoL/RMA+1gwnI9rn\nJyriAeDTAmBqh6mzEJmS8ZHZunZSWCuxLtMz6piqdFAZ0DMxaXCi9dWpSuut3vpV\nvHZ9JvZrpQvcnlRY/xyt++XsCctfwDKeDLi6LqQao8DpIJrlBdIVAF//AoGATMIf\nLeMOX+4mf1V1Nqxy41MgQFa1Z/aSXWXOTX9tZdLOKAPoMlhbonEDhZV3iYMEqnpn\nPBNZe8LCFLEZECj+7fJ8Cj5HvsKKLN4ol6gVoKWSmXknYALRiYeZXlnrZ6wPlPuC\n9U5piyuTb68BfEwgAtZrPulPGx8yhKlEjVIGcAECgYBM0NTSg/e1bc3hxyCdnFUt\nAmmon6JYJiv6zxx/b3rrtPkA3yuLwXTwlnFMWlmN+sSAVzaJ6ThYZ9lRYfwES+3Y\n5hCmcbaFU3xY8avKqAjs/984zv7eqK0xvUfgNUYNtsb62ED2y9tHDanIr0KMQZrj\nmS0dJsaykus7iCG/rPfaig==\n-----END PRIVATE KEY-----\n",
			  "client_email": "1056587235583-compute@developer.gserviceaccount.com",
			  "client_id": "101734015336513567516",
			  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
			  "token_uri": "https://accounts.google.com/o/oauth2/token",
			  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
			  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/1056587235583-compute%40developer.gserviceaccount.com"
			}"""

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