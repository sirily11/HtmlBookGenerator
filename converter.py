from htmlparser.htmlGenerator import HTMLGenerator
from htmlparser.markdownparser import Markdown
import os


if "speechtotext" not in os.path.basename(os.getcwd()):
    print("You should put this file in the doc file")

color = input("Color theme[in hex]: ")
print("Start the html conversion")
text_dir = "pages/text"
markdown = Markdown(file_dir=text_dir)
html = HTMLGenerator(markdown_parser=markdown)
if len(color) > 3:
    html.output_HTML(color)
else:
    html.output_HTML()
print("Finished")
input("Press any key to quit")