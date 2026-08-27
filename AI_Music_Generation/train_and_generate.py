
from pathlib import Path
import numpy as np
from music21 import converter, note, chord, stream
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

DATA_DIR = Path("midi_dataset")
OUT_DIR = Path("generated")
OUT_DIR.mkdir(exist_ok=True)

def extract_tokens(path):
    score = converter.parse(path)
    tokens = []
    for element in score.flatten().notes:
        if isinstance(element, note.Note):
            tokens.append(str(element.pitch))
        elif isinstance(element, chord.Chord):
            tokens.append(".".join(str(p) for p in element.pitches))
    return tokens

files = list(DATA_DIR.glob("*.mid")) + list(DATA_DIR.glob("*.midi"))
if not files:
    raise SystemExit("No MIDI files found. Run create_seed_midi.py first.")

sequences = []
for f in files:
    sequences.extend(extract_tokens(f))

if len(sequences) < 40:
    raise SystemExit("Not enough notes. Add more MIDI files to midi_dataset/.")

vocab = sorted(set(sequences))
to_int = {x:i for i,x in enumerate(vocab)}
encoded = np.array([to_int[x] for x in sequences], dtype=np.int32)

seq_len = 32
X, y = [], []
for i in range(len(encoded)-seq_len):
    X.append(encoded[i:i+seq_len])
    y.append(encoded[i+seq_len])
X = np.array(X)
y = np.array(y)

model = Sequential([
    LSTM(256, input_shape=(seq_len,1), return_sequences=True),
    Dropout(.2),
    LSTM(128),
    Dense(128, activation="relu"),
    Dense(len(vocab), activation="softmax"),
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

X_norm = X.astype("float32") / max(1, len(vocab)-1)
model.fit(X_norm[...,None], y, epochs=40, batch_size=32, validation_split=.1,
          callbacks=[EarlyStopping(patience=5, restore_best_weights=True)])

# Temperature sampling
rng = np.random.default_rng(42)
seed = X[-1].copy()
generated = []

for _ in range(160):
    inp = (seed.astype("float32") / max(1, len(vocab)-1))[None,...,None]
    probs = model.predict(inp, verbose=0)[0]
    probs = np.power(probs + 1e-9, 1/0.9)
    probs = probs / probs.sum()
    idx = rng.choice(len(vocab), p=probs)
    generated.append(vocab[idx])
    seed = np.append(seed[1:], idx)

score = stream.Stream()
for token in generated:
    if "." in token:
        pitches = token.split(".")
        score.append(chord.Chord(pitches, quarterLength=.5))
    else:
        score.append(note.Note(token, quarterLength=.5))

output = OUT_DIR / "generated_music.mid"
score.write("midi", fp=output)
print("Saved:", output)
