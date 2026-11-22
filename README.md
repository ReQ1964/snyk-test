# Snyk Test Calculator

Prosta aplikacja konsolowa typu kalkulator, przygotowana do testow w Snyk.

Projekt zawiera kilka celowo przestarzalych zaleznosci w `pyproject.toml`, aby
narzedzia typu Snyk mogly wykryc znane podatnosci lub stare wersje bibliotek.
Nie uzywaj tych wersji w prawdziwej aplikacji produkcyjnej.

## Uruchomienie

```bash
PYTHONPATH=src python -m snyk_calculator
```

Po instalacji projektu jako pakiet mozna tez uzyc:

```bash
pip install -e .
calculator
```

## Test Snyk

```bash
snyk auth
snyk test
```

Mozesz tez zaimportowac repozytorium lub katalog projektu w panelu
[Snyk](https://app.snyk.io/).
