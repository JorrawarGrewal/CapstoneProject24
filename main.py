import face_recognition
import cv2
import csv
import os
from datetime import datetime
import pickle
from calculateclassperiod import getclasspd, late_or_not
import email, smtplib, ssl, time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = #
password = #
receiver_emails = #

student_info = {}
reader = csv.reader(open('studentsinfo.csv'))
for row in reader:
    key = row[0]
    student_info[key] = row[1:]
print(student_info)


def send_email():
    global class_period, current_date, f
    f.close()
    subject = "Attendance for " + current_date + " " + class_period + " period"
    body = "This is an email with attachment sent from Python"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_emails
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    filename = 'attendancerecords/' + current_date + '-period' + class_period + '.csv'

    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_emails, text)

    print("SENT EMAIL")


video_capture = cv2.VideoCapture(0)

known_faces_ids = []

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
class_period = getclasspd()

for filename in os.listdir('db/{}'.format(class_period)):
    f = os.path.join('db/{}'.format(class_period), filename)
    if os.path.isfile(f):
        known_faces_ids.append(filename[:-7])

video_capture = cv2.VideoCapture(0)

face_locations = []
face_encodings = []
face_names = []
s = True

students = known_faces_ids.copy()
print(students)


f = open('attendancerecords/' + current_date + '-period' + class_period + '.csv', 'w+', newline='')
lnwriter = csv.writer(f)
lnwriter.writerow(['studentid', 'firstname', 'lastname', 'H:M:S', 'status'])


def update():
    global current_date, class_period, face_locations, face_encodings, face_names, s, filename, f, students, lnwriter,\
        known_faces_ids
    current_date = now.strftime("%Y-%m-%d")
    prev_classpd = class_period
    class_period = getclasspd()
    # updates all variables and opens new csv file
    if prev_classpd != class_period:
        if len(students) != 0:
            for student in students:
                lnwriter.writerow([student, student_info[student][0], student_info[student][0], 'ABSENT', 'ABSENT'])
        send_email()
        known_faces_ids = []
        for filename in os.listdir('db/{}'.format(class_period)):
            f = os.path.join('db/{}'.format(class_period), filename)
            if os.path.isfile(f):
                known_faces_ids.append(filename[:-7])
        face_locations = []
        face_encodings = []
        face_names = []
        s = True

        students = known_faces_ids.copy()
        print(students)

        f = open('attendancerecords/' + current_date + '-period' + class_period + '.csv', 'w+', newline='')
        lnwriter = csv.writer(f)
        lnwriter.writerow(['studentid', 'firstname', 'lastname', 'H:M:S', 'status'])


while True:
    embeddings_unknown = face_recognition.face_encodings(video_capture.read()[1])
    if len(embeddings_unknown) == 0:
        print('no persons found')
    else:
        embeddings_unknown = embeddings_unknown[0]

        db_dir = sorted(os.listdir('db/{}'.format(class_period)))

        match = False
        j = 0
        while not match and j < len(db_dir):
            path_ = os.path.join('db/{}'.format(class_period), db_dir[j])

            file = open(path_, 'rb')
            embeddings = pickle.load(file)

            match = face_recognition.compare_faces([embeddings], embeddings_unknown)[0]
            j += 1

        if match:
           name = db_dir[j - 1][:-7]
           if name in students:
               students.remove(name)
               current_time = now.strftime("%H:%M:%S")
               attendance = late_or_not()
               lnwriter.writerow([name, student_info[name][0], student_info[name][1], current_time, attendance])

        else:
            print('unknown_person')
    update()
