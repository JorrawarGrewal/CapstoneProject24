# makes encodings of all files in the pictures directory
import os
import face_recognition
import pickle

directory = 'pictures'


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        try:
            img = face_recognition.load_image_file(f)
            embeddings = face_recognition.face_encodings(img)[0]

            file = open(os.path.join('db/{}'.format(filename[9]), '{}.pickle'.format(filename[:-6])), 'wb')
            pickle.dump(embeddings, file)

        except:
            print("CANNOT FIND FACE IN " + f)
