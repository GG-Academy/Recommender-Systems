# Dataset: Top Hits Spotify 2000-2019

## Domeniu

Muzica. Dataset-ul contine melodiile cele mai populare de pe Spotify din perioada 2000-2019 (in date apar si cateva piese din 1998-1999 si 2020). Fiecare rand este o melodie.

- **Sursa:** [Top Hits Spotify from 2000-2019 (Kaggle)](https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019)
- **Fisier:** [`songs_normalize.csv`](songs_normalize.csv)
- **Numar de intrari:** 2000 de melodii

## Proprietati inregistrate in Recombee

- `artist` (`string`): numele artistului
- `song` (`string`): titlul melodiei
- `duration_ms` (`int`): durata melodiei, in milisecunde
- `year` (`int`): anul lansarii
- `popularity` (`int`): scorul de popularitate Spotify (0-100)
- `genre` (`set`): genurile melodiei- o melodie poate avea mai multe

## Incarcarea datelor in Recombee

Toate cele 2000 de melodii au fost incarcate cu succes in Recombee cu `recombee_items.py`. Dataset-ul original nu avea coloana de ID, asa ca am adaugat in CSV coloana `id` (`0`-`1999`), care este legata de `itemId` in Recombee.
