## Instalacion

```powershell
pip install pytest pytest-cov behave mutmut
```

> mutmut necesita Linux/WSL (usa fork(), no funciona en Windows nativo).

---

## Unidad II

```powershell
cd "Unidad_ii_Testing Orientado a Objetos"

python -m pytest ejercicio_1/tests/ -v
python -m pytest ejercicio_4/ -v
python -m pytest ejercicio_5/tests/ -v

mvn -f ejercicio_2/pom.xml test
mvn -f ejercicio_3/pom.xml test
```

---

## Unidad III

### Ejercicio 1

```powershell
cd "Unidad_III_Testing de_Integracio_Regresion_Mutacional_Aceptacion_CICD/Ejercicio1"

python -m pytest tests/test_inciso_1_ab.py -v
```

### Ejercicio 2

```powershell
cd "Unidad_III_Testing de_Integracio_Regresion_Mutacional_Aceptacion_CICD/Ejercicio2"

python -m pytest tests/ -v
```

### Ejercicio 3

```powershell
cd "Unidad_III_Testing de_Integracio_Regresion_Mutacional_Aceptacion_CICD/Ejercicio3"

python -m pytest tests/ -v

wsl -d Ubuntu mutmut run --paths-to-mutate=modelo/auto.py
wsl -d Ubuntu mutmut results
```

### Ejercicio 4

```powershell
cd "Unidad_III_Testing de_Integracio_Regresion_Mutacional_Aceptacion_CICD/flota_bdd"

behave features/
```

### Ejercicio 5

Pipeline en `.github/workflows/ci.yml`. Corre en GitHub Actions con push a develop/main o PR a main.

```powershell
cd "Unidad_III_Testing de_Integracio_Regresion_Mutacional_Aceptacion_CICD"

python -m pytest Ejercicio2/tests/ Ejercicio3/tests/ --cov=Ejercicio2/modelo --cov=Ejercicio3/modelo --cov-report=xml --cov-fail-under=80 -v

cd flota_bdd
behave features/
```
