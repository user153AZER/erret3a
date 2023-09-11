from bs4 import BeautifulSoup

html_code = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Controlled Brightness in a Lamp</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div class="lamp-wrapper">
<div class="lamp-rope"></div>
<div class="lamp">
<div class="lamp-part -top"></div>
<div class="lamp-part -top part"></div>
<div class="lamp-part top part right"></div>
</div>
<div class="lamp-part -body"></div>
<div class="lamp-part body right"></div>
<div class="lamp-part -bottom"></div>
<div class="blub"></div>
</div>
<div class="wall-light-shadow"></div>
<form oninput="body.setAttribute('data-light, slider.value)">
<div class="icon sun">
<div class="ray"></div>
<div class="ray"></div>
<div class="ray"></div>
<div class="ray"></div>
<div class="ray"></div>
<div class="ray"></div>
<div class="rays"></div>
<div class="ray"></div>
</div>
<input type="range" id="slider" value="80" min="0" max="10">
</form>
</body>
</html>
'''

soup = BeautifulSoup(html_code, 'html.parser')

# Extracting the title
title = soup.title.string
print("Title:", title)

# Extracting the CSS file
css_file = soup.find('link')['href']
print("CSS File:", css_file)

# Extracting the lamp parts
lamp_parts = soup.find_all(class_='lamp-part')
print("Lamp Parts:")
for part in lamp_parts:
    print(part['class'])

# Extracting the slider value
slider_value = soup.find('input', id='slider')['value']
print("Slider Value:", slider_value)
