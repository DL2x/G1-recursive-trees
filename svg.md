# Erklärung des .svg Formats

**s** = scaleable

**v** = vector

**g** = grafic

## Funktion

Punkte können Kommazahlen sein,

Bild wird an Pfaden je nach Auflösung generiert

## Vorteile

nur xml (text)    ->  einfach zu generieren

vector basiert    ->  Scallierung egal

## Nutzung / Beispiele
### Init:
```xml
<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1000">
```
### Linie:
```xml
<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" />
```
### Rechteck:
```xml
<rect x="0" y="0" width="{width}" height="{height}" fill="{colour}" />
```
*Note:* x & y müssen nicht gegeben werden und werden automatisch auf 0|0

### Verschieben:
```xml
<g transform="translate({x},{y})">
```
### Drehen:
```xml
<g transform="rotate({rot},{x},{y})">
```

### Andere Formen:

SVG unterstüzt auch noch andere Formen:
 - Kreis, 
 - Elipse,
 - Polygon,
 - Text,
 - ...


## Nutzung in dem Projekt
### Setzen des Headers:
```python
svg_header = '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1000">'

to_file(svg_header)
```

### Hintergrund weiß ausfüllen:
```python
to_file(f'<rect width="{str(width)}" height="{str(height)}" fill="#FFFFFF" />')
```

### Linie:
```python
def line(self, x1: float, y1: float, x2: float, y2: float, width: float, colour: str):
    line_str = f'<line x1="{str(x1)}" y1="{str(y1)}" x2="{str(x2)}" y2="{str(y2)}" stroke="{colour}" stroke-width="{str(width)}" />'
    to_file(line_str)
```

### Setzen des Footers
```python
svg_footer = '</svg>'

to_file(svg_footer)
```
