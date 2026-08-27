
from pathlib import Path
from music21 import stream, note, chord, tempo, meter, instrument

OUT = Path("midi_dataset")
OUT.mkdir(exist_ok=True)

patterns = [
    ["C4","E4","G4","C5","G4","E4","D4","F4"],
    ["A3","C4","E4","A4","E4","C4","B3","D4"],
    ["F3","A3","C4","F4","C4","A3","G3","B3"],
    ["G3","B3","D4","G4","D4","B3","A3","C4"],
]

for idx, pattern in enumerate(patterns):
    s = stream.Stream()
    s.append(tempo.MetronomeMark(number=100))
    s.append(meter.TimeSignature("4/4"))
    s.append(instrument.Piano())
    for repeat in range(8):
        for pitch in pattern:
            n = note.Note(pitch)
            n.quarterLength = 0.5
            s.append(n)
    s.write("midi", fp=OUT / f"seed_{idx+1}.mid")

print(f"Created {len(patterns)} seed MIDI files in {OUT}/")
