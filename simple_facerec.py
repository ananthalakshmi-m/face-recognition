import face_recognition
import cv2
import os
import glob
import numpy as np

class SimpleFacerec:
    def __init__(self):
        # Stores encodings of known faces
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frames for faster processing
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        """
        Load and encode all images from the given directory.
        Each image filename is used as the person's name.
        """
        # Get all image file paths
        images_path = glob.glob(os.path.join(images_path, "*.*"))
        print(f"{len(images_path)} encoding images found.")

        # Encode each image
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Extract filename (used as the label for the face)
            basename = os.path.basename(img_path)
            filename, _ = os.path.splitext(basename)

            # Generate face encoding
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Save the encoding and corresponding name
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)

        print("Encoding images loaded successfully.")

    def detect_known_faces(self, frame):
        """
        Detect faces in the given frame and match them with known faces.
        Returns the face locations and corresponding names.
        """
        # Resize frame for faster face detection
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)

        # Convert BGR (OpenCV default) to RGB (face_recognition requirement)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Detect all face locations and encodings in the frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Compare detected face with known faces
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # Select the known face with the smallest distance
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

            face_names.append(name)

        # Adjust face locations to match original frame size
        face_locations = np.array(face_locations) / self.frame_resizing
        return face_locations.astype(int), face_names