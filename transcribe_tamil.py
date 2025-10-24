import whisper

model = whisper.load_model('medium')
LANGUAGE = 'ta'

def transcribe_audio(audio_path, output_path):
	result = model.transcribe(audio_path, task='transcribe', language=LANGUAGE)
	tamil_text = result['text']
	with open(output_path, 'w', encoding='utf-8') as f:
		f.write(tamil_text)
