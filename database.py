import sqlite3
conn = sqlite3.connect('portal_final.db')

c = conn.cursor()
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS login_details
             (username varchar PRIMARY KEY , password varchar)''')
# Save (commit) the changes
conn.commit()



c_register = conn.cursor()
c_register.execute('''CREATE TABLE IF NOT EXISTS register
             (firstname varchar,lastname varchar, department varchar,post varchar,username varchar NOT NULL PRIMARY KEY , pwd varchar,email varchar,mobile varchar,address varchar)''')
conn.commit()


attendance_whole=conn.cursor()
attendance_whole.execute('''CREATE TABLE IF NOT EXISTS attendance_whole(ID varchar NOT NULL PRIMARY KEY,date varchar,status varchar)''')
conn.commit()

admin_register=conn.cursor()
admin_register.execute('''CREATE TABLE IF NOT EXISTS admin_register(ID varchar NOT NULL PRIMARY KEY,firstname varchar,lastname varchar,department varchar,post varchar)''')
conn.commit()

salary=conn.cursor()
salary.execute('''CREATE TABLE IF NOT EXISTS attendance_whole(ID varchar NOT NULL PRIMARY KEY,date varchar,salary varchar)''')
conn.commit()

message=conn.cursor()
message.execute('''CREATE table if not exists message_alerts(message varchar,date varchar)''')
conn.commit()

leave=conn.cursor()
leave.execute('''CREATE TABLE IF NOT EXISTS leave_requests(username varchar,from_date varchar,to_date varchar,reason varchar)''')
conn.close()
