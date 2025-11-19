# G1 - Rekursive Figuren / Bäume

![titel_bild](assets/image.png)


Dieses Programm erstellt rekursive Figuren und speichert sie in einer SVG datei ab.

Ihr könnt ruhig selbst mit dem Programm rumspielen.  
Dafür müsst ihr nur das Programm runterladen und die konstanten Variablen in dem ```## SETTINGS ##``` Abschnitt nach belieben verändern.

## Vokabeln & Vorwissen

Dieses Programm macht viel mit dem SVG Standart. Mehr zu wie es das macht und eine kleine Übersicht [hier](docs/svg.md).

## Einstellungen

*Note*: Nur ein kurzer Überblick!  
*Note*: Einige Erklärungen machen möglicheweise keinen Sinn, wenn ihr das Programm nicht versteht

| Einstellung        | mögliche Werte | Erklärung                              |
| :----------------- | :------------- | :------------------------------------- |
| **General**                                                                  |
| ```mode```         | "line", "quad" | Die Formen, die erstellt werden sollen |
| **Board**                                                                    |
| ```heigth```       | pos. float     | Die Höhe des SVGs                      |
| ```width```        | pos. float     | Die Breite des SVGs                    |
| **Size**                                                                     |
| ```initial_size``` | pos. float     | die Größe der ersten Generation        |
| ```dropoff```      | float          | wie schnell die Größe & Linienbreite sich verändert |
| ```exponential_dropoff``` | bool    | ob die Größe exponentiell kleiner werden soll |
| ```line_width```   | pos. float     | die Linienbreite, abhänging von der Länge  |
| **Colour**                                                                   |
| ```colour_background``` | hex colour str | Die Farbe des Hintergrundes. ```None``` für keine |
| ```colour_lines``` | hex colour str | Die Farbe der linien. ```None``` für keine |
| **Generations & Children**                                                   |
| ```max_generations``` | pos. int    | Die anzahl an generationen, die generiert werden sollen |
| ```children_count```| pos int       | Wie viele children jedes mal generiert werden sollen |



## Kurzer Überblick des Programmes

Importieren des "math" modules für sinus, cosinus, pi, etc:

```python
import math
```