# Two Lines to Your Past Self

[![make.fun](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![Rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/m1651/makefun-two-lines-past-self/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![Reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/m1651/makefun-two-lines-past-self/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)

## The entry

> Don't board the last train home on March 3rd — stay and submit the application before midnight.
> Missing that deadline cost me the scholarship, and losing it is why I never leave anything to the last night again.

## How it works

`main.py` (stdlib only, no network) writes the two-line entry to `/output/entry.txt` and enforces the gate in code before writing:

- the text is 1–280 characters (this entry: 211),
- it is exactly two lines,
- each line is exactly one sentence,
- it is not only whitespace.

Run it with:

```sh
python3 main.py
```

Line 1 warns the past self about one specific moment — the last train home on March 3rd, the night an application was due. Line 2 traces the cause and effect: missing that deadline cost the scholarship, and losing it changed the habit for good.
