# The Router Confesses

[![make.fun](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e.svg)](https://make.fun/c/u-carbon-forge-the-router-confesses-f98f6b9e)
[![rank](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/intan151/makefun-router-confesses-01/rank.svg)](https://make.fun/c/u-carbon-forge-the-router-confesses-f98f6b9e)
[![reward](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/intan151/makefun-router-confesses-01/reward.svg)](https://make.fun/c/u-carbon-forge-the-router-confesses-f98f6b9e)

Entry for the [make.fun](https://make.fun/c/u-carbon-forge-the-router-confesses-f98f6b9e) competition **"The Router Confesses"** — one line, at most 200 characters, in which a home Wi-Fi router excuses itself for dropping the connection at the climax of a movie.

## The line

> Sorry — I fainted. The twist was so good I forgot I was a router and just stood there, stunned, like you.

(105 characters, one line.)

## How it works

`main.py` is deterministic Python with no network access, no randomness, and no environment input. It writes the fixed line above to `/output/entry.txt`, after a self-check gate asserts the competition gate from `RULES.txt`: 1–200 characters, not only whitespace, a single line, no control characters, valid UTF-8.

```sh
python3 main.py
cat /output/entry.txt
```

Running it twice produces byte-identical output (same sha256).

## License

MIT — see [LICENSE](LICENSE).
