# Note CLI (Command Line Interface)

Aceste comenzi sunt utile pentru explorarea rapidă a setului de date fără a deschide un editor greoi.

### 1. Numărarea înregistrărilor
Verificăm câte rânduri au fișierele (inclusiv header-ul).
```bash
wc -l data/raw/*.csv
Util pentru a verifica volumul total de date.
```
2. Inspectarea primelor rânduri
Vedem structura coloanelor și separatorul.


```bash

head -n 5 data/raw/records_2022.csv
```
Ajută la identificarea rapidă a formatului (CSV vs TSV).

3. Căutarea înregistrărilor "cancelled"
Găsim toate tranzacțiile anulate în datele din 2023.

```Bash

grep -i "cancelled" data/raw/records_2023.csv | head
```
Comanda grep filtrează liniile care conțin textul specificat.

4. Verificarea coloanei 'Category'
Extragem coloana 3 (Category), o sortăm și numărăm valorile unice pentru a găsi greșeli de scriere.

```Bash

cut -d ',' -f 3 data/raw/records_2022.csv | sort | uniq -c
```
Rezultatul arată inconsecvențe precum "medication" vs "MEDICATION".

5. Combinarea rapidă a fișierelor
Concatenăm fișierele raw într-unul singur temporar pentru analiză globală.

```Bash

cat data/raw/*.csv > data/interim/all_raw_preview.csv
```

---
