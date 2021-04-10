import cv2


class WebCam:
    def get_frame(self, capture):
        while True:
            hasFrame, frame = capture.read()

            if not hasFrame:
                raise Exception("Camera frame not obtained")

            _, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
