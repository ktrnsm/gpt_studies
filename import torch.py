import torch
from transformers import Wav2Vec2ForCTC,Wav2Vec2Tokenizer
import torchaudio   
torchaudio.set_audio_backend("soundfile")

wav_path= "C:/Users/Şebnem/Documents/GitHub/gpt_studies/.wav"

model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
waveform, sample_rate = torchaudio.load(wav_path)
input_values = tokenizer(waveform[0], return_tensors='pt').input_values

with torch.no_grad():
    logits = model(input_values).logits
predicted_ids = torch.argmax(logits, dim=-1)
transcriptions = tokenizer.batch_decode(predicted_ids)

output_file = "C:/Users/Şebnem/Documents/GitHub/gpt_studies/transcriptions.txt"
with open(output_file, 'w') as f:
    for transcription in transcriptions:
        f.write(transcription + "\n")