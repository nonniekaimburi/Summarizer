def transcribe_audio(audio_file_path):
    with open(audio_file_path, "rb") as f:
        audio_data = f.read()
    
    response = openai.Audio.create(file=audio_data, model="gpt-4.0-turbo")
    return response.text
