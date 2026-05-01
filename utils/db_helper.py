import sqlite3

class DatabaseHelper:
    
    def __init__(self,db_path="test_bookings.db"):
     self.conn = sqlite3.connect(db_path)
     self.cursor = self.conn.cursor()
     self._create_table()

    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY,
            firstname TEXT,
            lastname TEXT,
            totalprice REAL,
            checkin TEXT,
            checkout TEXT
            )        
        """)
        self.conn.commit()

    def insert_booking(self, booking_id, data):
        self.cursor.execute(
        "INSERT INTO bookings VALUES (?, ?, ?, ?, ?, ?)",(
            booking_id,
            data["firstname"],
            data["lastname"],
            data["totalprice"],
            data["bookingdates"]["checkin"],
            data["bookingdates"]["checkout"]
            )
        )
        self.conn.commit()

    def get_booking(self, booking_id):
        self.cursor.execute(
            "SELECT * FROM bookings WHERE id = ?",(booking_id,)
        )
        return self.cursor.fetchone()

    def delete_booking(self, booking_id):
        self.cursor.execute( "DELETE FROM bookings WHERE id = ?",(booking_id,))
        self.conn.commit()

    def get_all_bookings(self):
        self.cursor.execute("SELECT * FROM bookings")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()