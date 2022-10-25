from os.path import isfile

base = lambda title, description: f'''<div align="center">
  <img src="img/icon.png" />
  <h1>{title}</h1>
  <h2>{description}</h2>
  <img src="https://img.shields.io/github/license/EvanHsieh0415/github-template">
</div>'''

i18n = {
  "zh_tw": (
    "Github範例", 
    "這裡可以放描述"
  ),
  "zh_cn": (
    "Github示例",
    "这里可以放描述"
  ),
}

for code, data in i18n.items():
  if not isfile(filename:=f"./{code}.md"):
    with open(filename, "w", encoding="utf8") as file:
      file.write(base(*data))