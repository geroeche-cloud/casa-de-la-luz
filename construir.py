#!/usr/bin/env python3
"""Arma la versión web independiente del sitio en docs/ (la que publica GitHub Pages).

index.html es la fuente: no lleva <html> ni <head> porque así se publica como artifact.
Este script le agrega esa envoltura y copia las lecturas.

Uso:  python3 construir.py
"""
import pathlib
import shutil

AQUI = pathlib.Path(__file__).parent
DOCS = AQUI / "docs"

CABEZA = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0;font:14px system-ui,sans-serif}
img{max-width:100%}
[hidden]{display:none!important}
</style>
"""

DOCS.mkdir(exist_ok=True)
fuente = (AQUI / "index.html").read_text(encoding="utf-8")
(DOCS / "index.html").write_text(CABEZA + fuente + "\n</html>\n", encoding="utf-8")
(DOCS / ".nojekyll").write_text("", encoding="utf-8")

destino = DOCS / "lecturas"
if destino.exists():
    shutil.rmtree(destino)
shutil.copytree(AQUI / "lecturas", destino)

print("Listo: docs/index.html y", len(list(destino.glob("*.html"))), "lecturas")
