# Snyk Test Calculator

## Dokladne kroki uruchomienia i testu Snyk

1. Aktywuj srodowisko virtualenv:

```bash
source .venv/bin/activate
```

Po aktywacji powinienes zobaczyc `(.venv)` na poczatku prompta terminala.

2. Jesli w virtualenv nie ma `pip`, dodaj go:

```bash
python -m ensurepip --upgrade
```

3. Zainstaluj celowo przestarzale zaleznosci z `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Ten krok jest wazny, bo Snyk dla Pythona sprawdza zaleznosci z pliku oraz
pakiety zainstalowane w aktywnym srodowisku.

4. Zaloguj sie do Snyk:

```bash
snyk auth
```

5. Uruchom test Snyk:

```bash
snyk test --command=python3
```

Jesli chcesz wskazac interpreter z virtualenv bezposrednio, uzyj:

```bash
snyk test --command=.venv/bin/python
```

Kod wyjscia `1` jest tutaj normalny, jesli Snyk wykryje podatnosci.
