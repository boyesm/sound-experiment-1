from playsound import playsound

# from pydub import AudioSegment
# from pydub.playback import play

count = 1
sounds = ['kick', 'hat', 'snare', 'hat']
import simpleaudio as sa

while True:
    input('press enter to play next sound') # TODO: make this less janky
    wave_obj = sa.WaveObject.from_wave_file(f"/Users/malcolm/Documents/Programming/Projects/exactbuyer/sound-experiment-1/{sounds[(count%len(sounds))-1]}.wav")
    play_obj = wave_obj.play()
    count+=1
