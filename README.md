# Snyk Test Calculator

## Dokladne kroki uruchomienia i testu Snyk

1. Przejdz do katalogu projektu:

```bash
cd /Users/ReQ1964/Coding/Projects/snyk
```

2. Aktywuj srodowisko virtualenv:

```bash
source .venv/bin/activate
```

Po aktywacji powinienes zobaczyc `(.venv)` na poczatku prompta terminala.

3. Jesli w virtualenv nie ma `pip`, dodaj go:

```bash
python -m ensurepip --upgrade
```

4. Sprawdz, czy `pip` dziala:

```bash
python -m pip --version
```

5. Zainstaluj celowo przestarzale zaleznosci z `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Ten krok jest wazny, bo Snyk dla Pythona sprawdza zaleznosci z pliku oraz
pakiety zainstalowane w aktywnym srodowisku.

6. Uruchom kalkulator:

```bash
PYTHONPATH=src python -m snyk_calculator
```

7. Zaloguj sie do Snyk:

```bash
snyk auth
```

8. Uruchom test Snyk:

```bash
snyk test --command=python3
```

Jesli chcesz wskazac interpreter z virtualenv bezposrednio, uzyj:

```bash
snyk test --command=.venv/bin/python
```

9. Oczekiwany wynik:

```text
Tested 12 dependencies for known issues, found 25 issues
```

Kod wyjscia `1` jest tutaj normalny, jesli Snyk wykryje podatnosci.
