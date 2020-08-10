from config.dbconfig import pg_config
import psycopg2

class MusicDAO:
    def __init__(self):

        connect_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                         pg_config['user'],
                                                         pg_config['passwd'])
        self.conn = psycopg2._connect(connect_url)

################################################################################
#                           All  Categories                                    #
################################################################################
#TODO: this can be more performant using generators
# instead of returning a list you can use 'yield'
# inside the for loop and it will not waste as much memory as a list
    def getAllMusic(self):
        cursor = self.conn.cursor()
        query = "select * from music;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

################################################################################
#                    Individual  Categories                                    #
################################################################################

    def getMusicById(self, mid):
        cursor = self.conn.cursor()
        query = "select * from music where mid = %s;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    def getMusicByFilename(self, filename):
        cursor = self.conn.cursor()
        query = "select * from music where filename = %s;"
        cursor.execute(query, (filename,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByLabels(self, labels):
        cursor = self.conn.cursor()
        query = "select * from music where labels = %s;"
        cursor.execute(query, (labels,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByChordType(self, chordtype):
        cursor = self.conn.cursor()
        query = "select * from music where chordtype = %s;"
        cursor.execute(query, (chordtype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByTimestampbefore(self, timestampbefore):
        cursor = self.conn.cursor()
        query = "select * from music where timestampbefore = %s;"
        cursor.execute(query, (timestampbefore,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByTimestampafter(self, timestampafter):
        cursor = self.conn.cursor()
        query = "select * from music where timestampafter = %s;"
        cursor.execute(query, (timestampafter,))
        result = []
        for row in cursor:
            result.append(row)
        return result

################################################################################
#                        Double  Categories                                    #
################################################################################

    def getMusicByFilenameandLabels(self, filename, labels):
        cursor = self.conn.cursor()
        query = "select * from music where filename = %s and labels = %s;"
        cursor.execute(query, (filename, labels))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByFilenameandChordtype(self, filename, chordtype):
        cursor = self.conn.cursor()
        query = "select * from music where filename = %s and chordtype = %s;"
        cursor.execute(query, (filename, chordtype))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByFilenameandTimestampbefore(self, filename, timestampbefore):
        cursor = self.conn.cursor()
        query = "select * from music where filename = %s and timestampbefore = %s;"
        cursor.execute(query, (filename, timestampbefore))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByFilenameandTimestampafter(self, filename, timestampafter):
        cursor = self.conn.cursor()
        query = "select * from music where filename = %s and timestampafter = %s;"
        cursor.execute(query, (filename, timestampafter))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByFilenameandLabels(self, filename, labels):
        cursor = self.conn.cursor()
        query = "select * from music where filename = %s and labels = %s;"
        cursor.execute(query, (filename, labels))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByLabelsandChordtype(self, labels, chordtype):
        cursor = self.conn.cursor()
        query = "select * from music where labels = %s and chordtype = %s;"
        cursor.execute(query, (labels, chordtype))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByLabelsandTimestampbefore(self, labels, timestampbefore):
        cursor = self.conn.cursor()
        query = "select * from music where labels = %s and timestampbefore = %s;"
        cursor.execute(query, (labels, timestampbefore))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByLabelsandTimestampafter(self, labels, timestampafter):
        cursor = self.conn.cursor()
        query = "select * from music where labels = %s and timestampafter = %s;"
        cursor.execute(query, (labels, timestampafter))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByChordTypeandTimestampbefore(self, chordtype, timestampbefore):
        cursor = self.conn.cursor()
        query = "select * from music where chordtype = %s and timestampbefore = %s;"
        cursor.execute(query, (chordtype, timestampbefore))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByChordTypeandTimestampafter(self, chordtype, timestampafter):
        cursor = self.conn.cursor()
        query = "select * from music where chordtype = %s and timestampafter = %s;"
        cursor.execute(query, (chordtype, timestampafter))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByTimestampbeforeandTimestampafter(self, timestampbefore, timestampafter):
        cursor = self.conn.cursor()
        query = "select * from music where timestampbefore = %s and timestampafter = %s;"
        cursor.execute(query, (timestampbefore, timestampafter))
        result = []
        for row in cursor:
            result.append(row)
        return result

################################################################################
#                        Triple  Categories                                    #
################################################################################

    def getMusicByFilenameandLabelsandChordtype(self, filename, labels, chordtype):
            cursor = self.conn.cursor()
            query = "select * from music where filename = %s and labels = %s and chordtype = %s;"
            cursor.execute(query, (filename, labels, chordtype))
            result = []
            for row in cursor:
                result.append(row)
            return result

    def getMusicByFilenameandLabelsandTimestampbefore(self, filename, labels, timestampbefore):
        cursor = self.conn.cursor()
        query = "select * from music where filename = %s and labels = %s and timestampbefore = %s;"
        cursor.execute(query, (filename, labels, timestampbefore))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByFilenameandLabelsandTimestampafter(self, filename, labels, timestampafter):
            cursor = self.conn.cursor()
            query = "select * from music where filename = %s and labels = %s and timestampafter = %s;"
            cursor.execute(query, (filename, labels, timestampafter))
            result = []
            for row in cursor:
                result.append(row)
            return result

    def getMusicByFilenameandChordtypeandTimestampbefore(self, filename, chordtype, timestampbefore):
        cursor = self.conn.cursor()
        query = "select * from music where filename = %s and chordtype = %s and timestampbefore = %s;"
        cursor.execute(query, (filename, chordtype, timestampbefore))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByFilenameandChordtypeandTimestampafter(self, filename, chordtype, timestampafter):
            cursor = self.conn.cursor()
            query = "select * from music where filename = %s and chordtype = %s and timestampafter = %s;"
            cursor.execute(query, (filename, chordtype, timestampafter))
            result = []
            for row in cursor:
                result.append(row)
            return result

    def getMusicByFilenameandTimestampbeforeandTimestampafter(self, filename, timestampbefore, timestampafter):
        cursor = self.conn.cursor()
        query = "select * from music where filename = %s and timestampbefore = %s and timestampafter = %s;"
        cursor.execute(query, (filename, timestampbefore, timestampafter))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByLabelsandChordtypeandTimestampbefore(self, labels, chordtype, timestampbefore):
            cursor = self.conn.cursor()
            query = "select * from music where labels = %s and chordtype = %s and timestampbefore = %s;"
            cursor.execute(query, (labels, chordtype, timestampbefore))
            result = []
            for row in cursor:
                result.append(row)
            return result

    def getMusicByLabelsandChordtypeandTimestampafter(self, labels, chordtype, timestampafter):
        cursor = self.conn.cursor()
        query = "select * from music where labels = %s and chordtype = %s and timestampafter = %s;"
        cursor.execute(query, (labels, chordtype, timestampafter))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMusicByLabelsandTimestampbeforeandTimestampafter(self, labels, timestampbefore, timestampafter):
            cursor = self.conn.cursor()
            query = "select * from music where labels = %s and timestampbefore = %s and timestampafter = %s;"
            cursor.execute(query, (labels, timestampbefore, timestampafter))
            result = []
            for row in cursor:
                result.append(row)
            return result

    def getMusicByChordTypeandTimestampbeforeandTimestampafter(self, chordtype, timestampbefore, timestampafter):
        cursor = self.conn.cursor()
        query = "select * from music where chordtype = %s and timestampbefore = %s and timestampafter = %s;"
        cursor.execute(query, (chordtype, timestampbefore, timestampafter))
        result = []
        for row in cursor:
            result.append(row)
        return result

################################################################################
#                     Quadruple  Categories                                    #
################################################################################

    def getMusicByFilenameandLabelsandChordtypeandTimestampbefore(self, filename, labels, chordtype, timestampbefore):
            cursor = self.conn.cursor()
            query = "select * from music where filename = %s and labels = %s and chordtype = %s and timestampbefore = %s;"
            cursor.execute(query, (filename, labels, chordtype, timestampbefore))
            result = []
            for row in cursor:
                result.append(row)
            return result

    def getMusicByFilenameandLabelsandChordtypeandTimestampafter(self, filename, labels, chordtype, timestampafter):
            cursor = self.conn.cursor()
            query = "select * from music where filename = %s and labels = %s and chordtype = %s and timestampafter = %s;"
            cursor.execute(query, (filename, labels, chordtype, timestampafter))
            result = []
            for row in cursor:
                result.append(row)
            return result

    def getMusicByFilenameandChordtypeandTimestampbeforeandTimestampafter(self, filename, chordtype, timestampbefore, timestampafter):
            cursor = self.conn.cursor()
            query = "select * from music where filename = %s and chordtype = %s and timestampbefore = %s and timestampafter = %s;"
            cursor.execute(query, (filename, chordtype, timestampbefore, timestampafter))
            result = []
            for row in cursor:
                result.append(row)
            return result

    def getMusicByFilenameandLabelsandTimestampbeforeandTimestampafter(self, filename, labels, timestampbefore, timestampafter):
            cursor = self.conn.cursor()
            query = "select * from music where filename = %s and labels = %s and timestampbefore = %s and timestampafter = %s;"
            cursor.execute(query, (filename, labels, timestampbefore, timestampafter))
            result = []
            for row in cursor:
                result.append(row)
            return result

    def getMusicByLabelsandChordtypeandTimestampbeforeandTimestampafter(self, labels, chordtype, timestampbefore, timestampafter):
            cursor = self.conn.cursor()
            query = "select * from music where labels = %s and chordtype = %s and timestampbefore = %s and timestampafter = %s;"
            cursor.execute(query, (labels, chordtype, timestampbefore, timestampafter))
            result = []
            for row in cursor:
                result.append(row)
            return result

################################################################################
#                     Quintuple  Category                                      #
################################################################################

    def getMusicByFilenameandLabelsandChordtypeandTimestampbeforeandTimestampafter(self, filename, labels, chordtype, timestampbefore, timestampafter):
            cursor = self.conn.cursor()
            query = "select * from music where filename = %s and labels = %s and chordtype = %s and timestampbefore = %s and timestampafter = %s;"
            cursor.execute(query, (filename, labels, chordtype, timestampbefore, timestampafter))
            result = []
            for row in cursor:
                result.append(row)
            return result

################################################################################
#                  Insert, Update, and Delete                                  #
################################################################################

    def insert(self, filename, labels, chordtype, timestampbefore, timestampafter):
        cursor = self.conn.cursor()
        query = "insert into music(filename, labels, chordtype, timestampbefore, timestampafter) values (%s, %s, %s, %s, %s) returning mid;"
        cursor.execute(query, (filename, labels, chordtype, timestampbefore, timestampafter))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def update(self, mid, filename, labels, chordtype, timestampbefore, timestampafter):
        cursor = self.conn.cursor()
        query = "update music set filename = %s, labels = %s, chordtype = %s, timestampbefore = %s, timestampafter = %s where mid = %s;"
        cursor.execute(query, (filename, labels, chordtype, timestampbefore, timestampafter, mid,))
        self.conn.commit()
        return mid

    def delete(self, mid):
        cursor = self.conn.cursor()
        query = "delete from music where mid = %s;"
        cursor.execute(query, (mid,))
        self.conn.commit()
        return mid