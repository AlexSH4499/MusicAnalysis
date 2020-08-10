from flask import jsonify
from dao.musictable import MusicDAO

dao = MusicDAO

class MusicHandler:
    def build_music_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['filename'] = row[1]
        result['labels'] = row[2]
        result['chordtype'] = row[2]
        result['timestampbefore'] = row[2]
        result['timestampafter'] = row[2]
        return result
    
    def build_music_attributes(self, mid, filename, labels, chordtype, timestampbefore, timestampafter):
        result = {}
        result['mid'] = mid
        result['filename'] = filename
        result['labels'] = labels
        result['chordtype'] = chordtype
        result['timestampbefore'] = timestampbefore
        result['timestampafter'] = timestampafter
        return result
    
    def getAllMusic(self):
        music_list = dao.getAllMusic()
        result_list = []
        for row in music_list:
            result = self.build_music_dict(row)
            result_list.append(result)
        return jsonify(Music=result_list)

    def getMusicById(self, mid):
        row = dao.getMusicById(mid)
        if not row:
            return jsonify(Error="Music Not Found"), 404
        else:
            Music = self.build_music_dict(row)
        return jsonify(Music=Music)

    def searchMusic(self, args):
        dao = MusicDAO
        filename = args.get('filename')
        labels = args.get('labels')
        chordtype = args.get('chordtype')
        timestampbefore = args.get('timestampbefore')
        timestampafter = args.get('timestampafter')
        music_list = []
        if (len(args) == 5) and filename and labels and chordtype and timestampbefore and timestampafter:
            music_list = dao.getMusicByFilenameandLabelsandChordtypeandTimestampbeforeandtimestampafter(filename, labels, chordtype, timestampbefore, timestampafter)
        elif (len(args == 4)) and filename and labels and chordtype and timestampbefore:
            music_list = dao.getMusicByFilenameandLabelsandChordtypeandTimestampbefore(filename, labels, chordtype, timestampbefore)
        elif (len(args == 4)) and filename and labels and chordtype and timestampafter:
            music_list = dao.getMusicByFilenameandLabelsandChordtypeandTimestampafter(filename, labels, chordtype, timestampafter)
        elif (len(args == 4)) and filename and chordtype and timestampbefore and timestampafter:
            music_list = dao.getMusicByFilenameandChordtypeandTimestampbeforeandTimestampafter(filename, chordtype, timestampbefore, timestampafter)
        elif (len(args) == 2) and filename and labels:
            music_list = dao.getMusicByFilenameandLabels(filename, labels)
        elif (len(args) == 1) and filename:
            music_list = dao.getMusicByFilename(filename)
        elif (len(args) == 1) and labels:
            music_list = dao.getMusicByLabels(labels)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in music_list:
            result = self.build_music_dict(row)
            result_list.append(result)
        return jsonify(Music=result_list)
    
    def insertMusicJson(self, json):
        filename = json['filename']
        labels = json['labels']
        chordtype = json['chordtype']
        timestampbefore = json['timestampbefore']
        timestampafter = json['timestampafter']
        if filename and labels and chordtype and timestampbefore and timestampafter:
            mid = dao.insert(filename, labels, chordtype, timestampbefore, timestampafter)
            result = self.build_music_attributes(mid, filename, labels, chordtype, timestampbefore, timestampafter)
            return jsonify(Music=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateMusic(self, mid, form):
        if not dao.getMusicById(mid):
            return jsonify(Error="Music not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                filename = form['filename']
                labels = form['labels']
                chordtype = form['chordtype']
                timestampbefore = form['timestampbefore']
                timestampafter = form['timestampafter']
                if filename and labels and chordtype and timestampbefore and timestampafter:
                    dao.update(mid, filename, labels, chordtype, timestampbefore, timestampafter)
                    result = self.build_music_attributes(mid, filename, labels, chordtype, timestampbefore, timestampafter)
                    return jsonify(Music=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteMusic(self, mid):
        if not dao.getMusicById(mid):
            return jsonify(Error="Music not found."), 404
        else:
            dao.delete(mid)
            return jsonify(DeleteStatus="OK"), 200