[← Înapoi la indexul general](../../README.md) | 🇬🇧 English Version TBA

**Acces Rapid:** [📄 Vezi `track.py`](../track.py)

---

# Laborator 1: Colectarea Datelor Implicite în Sistemele de Recomandare

În sistemele de recomandare moderne, o mare parte din date sunt colectate implicit — fără ca utilizatorul să introducă manual note sau calificative. În acest laborator, veți rula un server local în Python care extrage metadatele contextuale transmise prin protocoalele HTTP (IP, profil dispozitiv, limbi preferate) și veți efectua o cerere de test utilizând un client HTTP (Postman, Insomnia, Thunder Client sau cURL).

## Cerințe preliminare

1. Asigurați-vă că ați configurat mediul virtual Python conform [Ghidului de instalare din rădăcină](../../README.md).
2. Asigurați-vă că aveți instalate pachetele din `requirements.txt`.
3. Aveți pregătit un client HTTP (ex: Postman, Insomnia, Thunder Client).

## Instrucțiuni de rulare

### 1. Porniți serverul din terminal

Asigurați-vă că ați descărcat fișierul [📄 `track.py`](../track.py) în directorul `lab01`, apoi rulați-l din terminal:

```bash
python track.py
```

### 2. Deschideți Postman (sau clientul preferat) și configurați cererea astfel:

- Metodă HTTP: `POST`
- URL: `http://127.0.0.1:5000/track`
- Headers: Adăugați `Content-Type: application/json`
- Body: Selectați opțiunea `raw` / `JSON` și trimiteți numele vostru complet:
```
{
  "student_name": "Nume Prenume"
}
```

### 3. Trimiteți cererea (Send) și copiați răspunsul JSON primit

## Instrucțiuni de predare

Salvați răspunsul JSON generat într-un fișier numit `track_Nume_Prenume.json` și încărcați-l pe platformă.

```
{
  "student": "Popescu Ion",
  "run_info": {
    "timestamp": 1772866200,
    "verification_hash": "a4f8b2e19c30"
  },
  "device_context": {
    "browser": "PostmanRuntime 7.36",
    "device_type": "Desktop",
    "os": "Windows 11",
    "raw_user_agent": "PostmanRuntime/7.36.0"
  },
  "network": {
    "ip_address": "127.0.0.1"
  },
  "user_preferences_implicit": {
    "preferred_language": "en-US"
  }
}
```
