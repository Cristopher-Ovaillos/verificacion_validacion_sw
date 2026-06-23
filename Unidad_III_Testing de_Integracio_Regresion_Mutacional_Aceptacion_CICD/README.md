# Comandos de ejecución

## Ejercicio 1 — Integración Bottom-Up

```
cd Ejercicio1
pytest tests/test_inciso_1_ab.py -v
pytest tests/test_inciso_2.py -v
pytest tests/test_inciso_3.py -v
pytest tests/test_inciso_5.py -v
```

## Ejercicio 2 — Regresión

```
cd Ejercicio2
pytest tests/test_auto_asignar.py -v
pytest tests/test_regresion_cambio_a.py -v
pytest tests/test_no_regresion_moto_camion.py -v
pytest tests/test_auto_registro.py -v
pytest tests/test_contaminacion_singleton.py -v
```

## Ejercicio 3 — Análisis Mutacional

```
cd Ejercicio3
pytest tests/test_auto_asignar.py -v

# mutmut (requiere WSL):
# wsl
# cd "/mnt/c/Users/jason/OneDrive/Documents/verificacion_validacion_sw/Unidad_III_Testing de_Integracio_Regresion_Mutacional_Aceptacion_CICD/Ejercicio3"
# mutmut run
# mutmut results
```
