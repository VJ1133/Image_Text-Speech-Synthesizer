from google.cloud import texttospeech
import os
text_to_speech = texttospeech.TextToSpeechClient()
image_text = 'quotes.txt'
with open(image_text, 'r') as files:
    text = files.read()
    value = texttospeech.types.SynthesisInput(text=text)
speech= texttospeech.types.VoiceSelectionParams(language_code='en-US',
                                                ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
configuration = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)
result  = text_to_speech.synthesize_speech(value, speech , configuration)
with open('file_output_speec1.mp3', 'wb') as final_speech:
    final_speech.write(result.audio_content)
