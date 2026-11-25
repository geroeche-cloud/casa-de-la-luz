# Casa de la Luz

Sitio de estudio de geometría sagrada y tradiciones espirituales: símbolos dibujados con su geometría, rituales y oraciones enteras, documentos oficiales desclasificados traducidos o resumidos, y lecturas largas sobre ángeles y el libro de Abramelín.

## Cómo está armado

- `index.html`: la página. Es la fuente; no lleva `<html>` ni `<head>`.
- `lecturas/`: una lectura larga por archivo. La página las abre en el lector.
- `construir.py`: arma la versión web independiente en `docs/`.
- `docs/`: lo que se publica en GitHub Pages. No se edita a mano.

## Cómo actualizar el sitio

1. Editar `index.html` o agregar un archivo en `lecturas/`.
2. Ejecutar `python3 construir.py`.
3. Subir los cambios:

```bash
git add -A && git commit -m "Actualiza el sitio" && git push
```

En uno o dos minutos el link público muestra la versión nueva.

## Sobre el contenido

Cada lectura dice al principio en qué documento se basa y qué partes no se pudieron leer o verificar. Los documentos del gobierno de EE. UU. son de dominio público. El informe de 1988 del National Research Council tiene derechos de autor y por eso va solo como resumen propio.
