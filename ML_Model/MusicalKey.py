import typing
from typing import Iterable

PITCHES =('C','C#','D','D#','E','F','F#','G','G#','A','A#','B')

MODES = ('major','minor')

class MusicKey:

    def __init__(self, pitch:str, mode:str):

        if self.is_valid_pitch(pitch):
            self.pitch = pitch
        else:
            self.pitch = None
        
        if self.is_valid_mode(mode):
            self.mode = mode
        else:
            self.mode = None

        return
    
    def pitch(self):
        return self.pitch
    
    def mode(self):
        return self.mode

    def is_valid_pitch(self, pitch:str)->bool:
        if pitch in PITCHES:
            return True
        return False
    
    def is_valid_mode(self, mode:str)->bool:
        if mode in MODES:
            return True
        return False

class MusicKeyFactory:

    def __init__(self):
        return
    
    def create_new_key(self, pitch:str, mode:str):

        key = MusicKey(pitch=pitch, mode=mode)

        try:
            self.is_valid_key(key)
        except Exception as e:
            print(e)
            key = None
        finally:
            pass

        return key
    
    def is_valid_key(self, key:MusicKey)->bool:

        if (not key.is_valid_mode(key.mode()) ) or (not key.is_valid_pitch(key.pitch())):

            raise ValueError("Sorry invalid MusicalKey provided")

        else:
            return True
    
    def create_all_keys(self, keys:Iterable[str], modes:Iterable[str]):

        keys=[]
        for mode in modes:
            for pitch in pitches:
                key = self.create_new_key(pitch,mode)
                if key:
                    keys.append(key)
        return keys

    