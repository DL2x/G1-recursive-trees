class SVGWriter:
  def __init__(self, file: str):
    self.svg_header = '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1000">'
    self.svg_footer = '</svg>'

    self.file = file

    self.file_clear()
    self.write(self.svg_header)

  def close(self):
    self.write(self.svg_footer)

  ## SVG FUNCTIONS ##
  def file_clear(self):
    open(self.file, 'w').close()

  def write(self, contents: str):
    try: 
      with open(self.file, 'a') as f: f.write(contents + "\n")
    except: 
      print("Error writing to svg file!")

  def line(self, x1: float, y1: float, x2: float, y2: float, width: float, colour: str):
    return f'<line x1="{str(x1)}" y1="{str(y1)}" x2="{str(x2)}" y2="{str(y2)}" stroke="{colour}" stroke-width="{str(width)}" />'

  def rect(self, width: float, height: str, colour: str):
    return f'<rect width="{str(width)}" height="{str(height)}" fill="{colour}" />'