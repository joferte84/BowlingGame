# Bowling Game Simulator

Este proyecto simula un juego de bolos, permitiendo a los jugadores lanzar bolos y calcular su puntuación a lo largo de un juego completo. La implementación se ha refactorizado al máximo para asegurar la legibilidad y mantenibilidad del código. Además, se han realizado pruebas exhaustivas para garantizar que la lógica del juego se comporta según lo esperado en diversas situaciones.

## Estructura del Proyecto

El proyecto consta de dos archivos principales:

- `BowlingGame_fac.py`: Define la clase `BowlingGame`, que simula la lógica de un juego de bolos.
- `test.py`: Contiene pruebas unitarias para la clase `BowlingGame`, asegurando que todas las funcionalidades se comportan correctamente. Añadiendo 3 tests mas a los requeridos inicialmente y un mockeo.

## Requisitos

Para ejecutar este proyecto, necesitas tener Python 3 instalado en tu máquina. No se requieren librerías externas adicionales, ya que solo se utiliza el módulo `unittest` de Python, el cual viene incluido en la instalación estándar de Python.

## Cómo Ejecutar

Primero, clona o descarga este repositorio en tu máquina local. Luego, puedes ejecutar el script de testeo para verificar que todo funciona correctamente:

```bash
python test.py
``` 

Esto ejecutará todas las pruebas unitarias definidas en test.py, mostrando los resultados en la consola. Si todas las pruebas pasan, significa que la implementación del juego de bolos funciona como se espera.

Si quieres ejecutar el juego necesitas ejecutar el script `BowlingGame_fac.py` desde tu terminal.

```bash
python BowlingGame_fac.py
```

## Contribuir
Si deseas contribuir al proyecto, por favor, asegúrate de agregar pruebas unitarias para cualquier nueva funcionalidad o corrección de errores para mantener la calidad y la estabilidad del código.
