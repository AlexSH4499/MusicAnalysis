import csv, typing
from Music_Analysis import utils.settings

from typing import List, Any, Iterable

class ChordFamily:

    def __init__(self, chord:str, mod:str):
        self.chord = chord
        self.modifier = mod
        return
    
    def chord(self)->str:
        return self.chord
    
    def modifier(self)->str:
        return self.modifier
    
    def __str__(self)->str:
        return f"{self.chord()}{self.modifier()}"
    
class ChordFactory:

    def __init__(self):
        return
    
    def new_chord(self, chord, mod)->ChordFamily:
        return ChordFamily(chord,mod)

class ChordFamilyBuilder:

    def __init__(self):
        self.chord_factory = ChordFactory()
        return
    
    def produce_chords(self, chords:Iterable[tuple(str,str)])->Iterable[ChordFamily]:
        for chord, mod in chords:
            yield self.chord_factory.new_chord(chord, mod)
    
    def read_chords_from(self, filename,root_dir = settings.setup()):
        
        file_path = settings.find(name=filename, path=root_dir)
        with open(file_path,'r') as cords:
            chords_reader = csv.reader(cords)
            for line in chords_reader:
                #ignore first line
                yield line


