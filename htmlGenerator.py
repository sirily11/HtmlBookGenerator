import os
class HTMLGenerator:
    def __init__(self):
        pass

    def __generate_menu__(self):
        pass

    def generate_tag(self, type="div", style="", id="", content="", src=""):
        if type != "input":
            tag = '<{} class="{}" id="{}">{}</{}>'.format(type, style, id, content, type)

        return tag


dir = "G:\\speechtotext\\pages\\video"
for root, dirs, files in os.walk(dir, topdown=False):
    for name in files:
        print(name)
    for name in dirs:
        print(name)