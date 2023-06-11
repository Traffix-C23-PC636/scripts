import cv2
from ultralytics import YOLO
import supervision as sv

url = "https://atcs-dishub.bandung.go.id:1990/Telkom/index.m3u8"
vcap = cv2.VideoCapture(url)
model = YOLO("./best.pt")

LINE_START = sv.Point(0, 0)
LINE_END = sv.Point(640, 640)


line_counter = sv.LineZone(start=LINE_START, end=LINE_END)
line_annotator = sv.LineZoneAnnotator(thickness=2, text_thickness=1, text_scale=0.5)
box_annotator = sv.BoxAnnotator(
    thickness=2,
    text_thickness=1,
    text_scale=0.5
)

while True:
    ret, frame = vcap.read()

    if frame is not None:
        results =  model.track(frame, stream=True, tracker="bytetrack.yaml", persist=True)

        for result in results:
            frame = result.orig_img
            detections = sv.Detections.from_yolov8(result)
            
            if result.boxes.id is not None:
                detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)


            labels = [] 
            # # i dunno what happen w/ the code below, I need some time to fix that, but its not that important 
            # # using empty array seems fix the issue

            # labels = [
            #     f"{tracker_id} {model.model.names[class_id]} {confidence:0.2f}"
            #     for _, confidence, class_id, tracker_id
            #     in detections
            # ]

            # labels = [
            #     f" {class_id}"
            #     for class_id
            #     in detections
            # ]

            frame = box_annotator.annotate(
                scene=frame, 
                detections=detections,
                labels=labels
            )

            line_counter.trigger(detections=detections)
            line_annotator.annotate(frame=frame, line_counter=line_counter)
            
            print(line_counter.in_count)
            print(line_counter.out_count)


            cv2.imshow('frame', frame)

        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print("Frame is None")
        break

vcap.release()
cv2.destroyAllWindows()
print("Video stop")