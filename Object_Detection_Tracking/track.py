
import argparse
import cv2
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser(description="YOLO multi-object tracking")
    parser.add_argument("--source", default="0", help="0 for webcam or a video path")
    parser.add_argument("--model", default="yolo26n.pt")
    parser.add_argument("--tracker", default="bytetrack.yaml")
    parser.add_argument("--conf", type=float, default=0.35)
    parser.add_argument("--output", default="tracked_output.mp4")
    args = parser.parse_args()

    source = int(args.source) if args.source.isdigit() else args.source
    model = YOLO(args.model)

    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open source: {args.source}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 640)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 480)

    writer = None
    if not isinstance(source, int):
        writer = cv2.VideoWriter(
            args.output, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)
        )

    # Ultralytics supports track mode with ByteTrack configuration.
    results = model.track(
        source=source,
        stream=True,
        persist=True,
        tracker=args.tracker,
        conf=args.conf,
        verbose=False
    )

    for result in results:
        frame = result.plot()
        cv2.imshow("CodeAlpha YOLO Object Tracking", frame)
        if writer is not None:
            writer.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    if writer:
        writer.release()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
