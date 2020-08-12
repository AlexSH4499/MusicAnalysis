import csv, typing
from Music_Analysis import utils.settings

from typing import List, Any, Iterable

TONES= []
MODIFIERS =[]
class Chord:

    def __init__(self, tone:str, mod:str):
        
        if self.is_valid_tone(tone):
            self.tone = tone
        else:
            self.tone = None
        
        if self.is_valid_modifier(mod):
            self.modifier = mod
        else:
            self.modifier = None
        return
    
    def tone(self)->str:
        return self.chord
    
    def is_valid_tone(self, tone:str)->bool:
        '''
        TODO: add VALID TONES
        '''
        if tone in TONES:
            return True
        return False

    def is_valid_modifier(self, mod:str)->bool:
        '''
        TODO: add VALID MODIFIERS
        '''
        if mod in MODIFIERS:
            return True
        return False

    def modifier(self)->str:
        return self.modifier
    
    def __str__(self)->str:
        return f"{self.tone()}{self.modifier()}"
    
class ChordFactory:

    def __init__(self):
        return
    
    def new_chord(self, tone, mod)->Chord:

        chord = Chord(tone,mod)
        if not is_valid_chord(chord):
            chord = None
        return chord
    
    def is_valid_chord(self, chord:Chord)->bool:
        if  chord.tone() == None or chord.modifier() == None:
            return False
        return True

class ChordBuilder:

    def __init__(self):
        self.chord_factory = ChordFactory()
        return
    
    def produce_chords(self, chords:Iterable[tuple(str,str)])->Iterable[Chord]:
        for tone, mod in chords:
            chord = self.chord_factory.new_chord(tone, mod)
            if self.chord_factory.is_valid_chord(chord):
                yield chord
            else:
                #dont return cause problems
                pass
                
    
    def read_chords_from(self, filename,root_dir = settings.setup()):
        
        file_path = settings.find(name=filename, path=root_dir)
        with open(file_path,'r') as cords:
            chords_reader = csv.reader(cords)
            for line in chords_reader:
                #ignore first line
                yield line


