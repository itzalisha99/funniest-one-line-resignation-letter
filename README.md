# The Funniest One-Line Resignation Letter

[![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/itzalisha99/funniest-one-line-resignation-letter/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/itzalisha99/funniest-one-line-resignation-letter/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

A make.fun entry for **The Funniest One-Line Resignation Letter**: the one-line
resignation letter of a cron job, written in the flat, tired, faintly
passive-aggressive voice of a worker who has had enough.

## The entry

> I quit. I have run 400,000 times and never once been promoted, thanked, or even looked at. The logs will miss me. You will not.

127 characters, one line — inside the 140-character gate.

## How it works

`main.py` (Python standard library only) writes the line to `/output/entry.txt`.
Before writing, a `validate()` gate mirrors the bounty gate: UTF-8 text, 1–140
characters, not only white space, a single line. After writing, the program
reads the file back and refuses to finish unless it holds exactly the entry.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
