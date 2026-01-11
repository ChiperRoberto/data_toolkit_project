# Note privind Formatele de Fișiere

## Strategia de Salvare
Pentru datele procesate, am ales să export două formate distincte, fiecare având un scop specific:

1. **CSV (`records_clean.csv`)**
   - **Motiv:** Este un format universal, citibil de oameni (human-readable) și poate fi deschis în orice editor de text sau Excel.
   - **Utilizare:** Inspecție rapidă și compatibilitate maximă.

2. **Parquet (`records_clean.parquet`)**
   - **Motiv:** Este un format binar, comprimat și orientat pe coloane.
   - **Avantaje:** Ocupă mai puțin spațiu pe disc și este mult mai rapid de citit pentru seturi mari de date în Python/R (păstrează tipurile de date corecte, spre deosebire de CSV unde totul poate deveni string).

## Evoluția Schemei
Datele originale au prezentat o evoluție a schemei ("Schema Drift"):
- **2022:** Nu conținea coloanele `department` și `priority`.
- **2023:** A introdus aceste coloane noi.

**Soluție:** Pipeline-ul a unificat schemele. Pentru înregistrările din 2022, coloanele noi au fost completate automat cu valori nule (`NaN`), permițând analiza unitară a întregului istoric.