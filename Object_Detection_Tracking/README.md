# CodeAlpha Task 4 — Object Detection and Tracking

## Requirements implemented
- OpenCV video/webcam input
- Pretrained YOLO object detection
- Bounding boxes and class labels
- Multi-object tracking
- Tracking IDs
- ByteTrack tracker configuration
- Real-time display
- Optional saved video output

## Run

```bash
pip install -r requirements.txt
python detect.py --source 0
python track.py --source 0
```

For a video:

```bash
python track.py --source input.mp4 --output tracked_output.mp4
```

Ultralytics' current Python documentation supports `YOLO(...).predict(...)` for image/video/webcam inference and `model.track(..., tracker="bytetrack.yaml")` for tracking.

The model weights are downloaded automatically by Ultralytics when required, so they are not bundled in this ZIP.
