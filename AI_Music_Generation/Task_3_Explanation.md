# Task 3 Explanation

### Pipeline
MIDI files → music21 parsing → note/chord tokens → integer encoding → fixed-length sequences → LSTM → next-token probability → sampled sequence → MIDI.

### Why LSTM?
Music is sequential. An LSTM can learn dependencies across previous notes and predict likely next notes.

### Important limitation
A four-file seed corpus is only a demonstration corpus. For a strong internship submission, train on a substantially larger public-domain MIDI collection and compare generated sequences qualitatively and quantitatively.
