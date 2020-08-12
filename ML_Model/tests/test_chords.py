import unittest
from unittest import TestCase
from ML_Model.ChordFamily import ChordFamily
from ML_Model.MusicalKey import MusicKey, MusicKeyFactory, PITCHES, MODES


class TestChords(TestCase):

    def test_creating_chords(self):
        # self.assertTrue()
        return

    def test_creating_keys(self):
        factory = MusicKeyFactory()

        for mode in MODES:
            for pitch in PITCHES:
                self.assertTrue(factory.create_new_key(mode=mode, pitch=pitch) != None)

        return





if __name__ == "__main__":
    unittest.main()