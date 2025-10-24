import os
import librosa
import soundfile as sf

def preprocess_audio(audio_path, output_path):
    try:
        # Load audio
        y, sr = librosa.load(audio_path, sr=None)
        if y is None or len(y) == 0:
            raise ValueError(f"Audio file '{audio_path}' could not be loaded or is empty. Please upload a valid audio file.")

        # Normalize audio
        y = y / max(abs(y))

        # Resample to 16kHz
        TARGET_SR = 16000
        if sr != TARGET_SR:
            y = librosa.resample(y, orig_sr=sr, target_sr=TARGET_SR)

        # Ensure preprocessed directory exists
        preprocessed_dir = os.path.dirname(output_path)
        if not os.path.exists(preprocessed_dir):
            os.makedirs(preprocessed_dir)

        # Save preprocessed audio
        sf.write(output_path, y, TARGET_SR)

        print(f"Preprocessed audio saved to: {output_path}")

    except Exception as e:
        print(f"Error processing {audio_path}: {e}")
        raise  # Properly re-raise the exception

