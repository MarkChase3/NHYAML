import yaml
import io

file = io.open('blog.yml')

dict = yaml.load(file, yaml.loader.FullLoader)

print(dict)
addstyle = ''
def parse(dict):
    global addstyle
    keys = list(dict.keys())
    if len(keys) == 0:
        return ''
    i = keys[0]
    type = i.split('#')[0]
    txt = dict[i]
    del dict[i]
    if type == 'center-text':
        return '<h1 style="text-align: center;  text-transform: capitalize; color: #ddf; font-family: \'Raleway\', sans-serif;font-weight: 300;font-size: 40px;' + addstyle + '">' + txt + '</h1>\n' + parse(dict)
    if type == 'text':
        return '<h1 style="color: #ddf; font-family: \'Raleway\', sans-serif;font-weight: 300;font-size: 20px;' + addstyle + '">' + txt + '</h1>\n' + parse(dict)
    if type == 'grid-5':
        addstyle = 'max-width: 13vw; margin: 2vw; width: 13vw; height: auto;'
        str = '<div style="display: flex; flex-wrap: wrap; margin: 4vw; height: auto">\n' + parse(txt) + '</div>\n'
        addstyle = ''
        return str + parse(dict)
    if type == 'fig':
        return  '<figure style = "' + addstyle + '"><img src="' + txt['src'] +'" style="image-rendering: pixelated; left: 25vw; width: 50vw; height: auto;' + addstyle + '"><figcaption style="text-align: center;  text-transform: capitalize; color: #ddf; font-family: \'Raleway\', sans-serif;font-weight: 300;font-size: 10px;' + addstyle + 'margin: 0 2vw;">' + txt['text'] + '</figcaption>\n</figure>\n' + parse(dict)
    if type == 'center-fig':
        return  '<figure style = "display:block; margin: auto;' + addstyle + '"><img src="' + txt['src'] +'" style="image-rendering: pixelated; left: 25vw; width: 50vw; height: auto;' + addstyle + '"><figcaption style="text-align: center;  text-transform: capitalize; color: #ddf; font-family: \'Raleway\', sans-serif;font-weight: 300;font-size: 10px;' + addstyle + 'margin: 0 2vw;">' + txt['text'] + '</figcaption>\n</figure>\n' + parse(dict)
    if type == 'fig-link':
        return  '<figure style = "' + addstyle + '"><a href="'+ txt['link'] +'"><img src="' + txt['src'] +'" style="left: 25vw; width: 50vw; height: auto; image-rendering: pixelated; text-align: center;' + addstyle + '"></a><figcaption style="text-transform: capitalize; color: #ddf; font-family: \'Raleway\', sans-serif;font-weight: 300;font-size: 10px;' + addstyle + 'margin: 0 2vw;">' + txt['text'] + '</figcaption>\n</figure>\n' + parse(dict)
    if type == 'center-fig-link':
        return  '<figure style = "' + addstyle + '"><a href="'+ txt['link'] +'"><img src="' + txt['src'] +'" style="display:block; margin: auto; width: 50vw; height: auto; image-rendering: pixelated; text-align: center;' + addstyle + '"></a><figcaption style="display:block; margin: auto;text-transform: capitalize; color: #ddf; font-family: \'Raleway\', sans-serif;font-weight: 300;font-size: 10px;' + addstyle + 'margin: 0 2vw;">' + txt['text'] + '</figcaption>\n</figure>\n' + parse(dict)
    return ''
print('<body style="background: #111;">')
print(parse(dict))
print('</body>')
