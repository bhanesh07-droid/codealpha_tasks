# CodeAlpha Task 3 — Music Generation with AI

## Requirements implemented
- MIDI collection directory
- MIDI parsing with music21
- Note/rest sequence extraction
- Sequence encoding
- LSTM deep-learning model
- Next-token prediction
- Generated MIDI output

## Dataset
Place MIDI files under:

```text
midi_dataset/
    *.mid
    *.midi
```

The notebook/script can also create a small original seed MIDI corpus with `create_seed_midi.py` so the pipeline can be tested without downloading copyrighted music.

For a stronger project, replace the seed corpus with a public-domain classical MIDI collection.

## Run

```bash
pip install -r requirements.txt
python create_seed_midi.py
python train_and_generate.py
```

Output:
`generated/generated_music.mid`
