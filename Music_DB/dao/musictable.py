from config.dbconfig import pg_config
import psycopg2

class MusicDAO:
    def __init__(self):

        connect_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                         pg_config['user'],
                                                         pg_config['passwd'])
        self.conn = psycopg2._connect(connect_url)

    def getAllMusic(self):
        cursor = self.conn.cursor()
        query = "select * from music;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

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

    def getMusicByFilenameandLabels(self, filename, labels):
        cursor = self.conn.cursor()
        query = "select * from music where filename = %s and labels = %s;"
        cursor.execute(query, (filename, labels))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, filename, labels):
        cursor = self.conn.cursor()
        query = "insert into music(filename, labels) values (%s, %s) returning mid;"
        cursor.execute(query, (filename, labels,))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def update(self, mid, filename, labels):
        cursor = self.conn.cursor()
        query = "update music set filename = %s, labels = %s where mid = %s;"
        cursor.execute(query, (filename, labels, mid,))
        self.conn.commit()
        return mid

    def delete(self, mid):
        cursor = self.conn.cursor()
        query = "delete from music where mid = %s;"
        cursor.execute(query, (mid,))
        self.conn.commit()
        return mid