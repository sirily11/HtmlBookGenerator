from tqdm import tqdm
import os
import mistune


class Markdown:
    def __init__(self, file_dir, renderer=""):
        self.html_content = []
        self.file_dir = file_dir
        self.dir_dict = self.generate_dir_dict()
        self.renderer = renderer

    def generate_dir_dict(self):
        dir_dict = []
        for root, dirs, files in os.walk(self.file_dir, topdown=False):
            dir_dict.append({
                "root": root,
                "folder_name": os.path.basename(root),
                "file_list": files
            })
        return dir_dict

    def read_markdown(self):
        print(self.file_dir)
        for l in tqdm(self.dir_dict):
            root = l['root']
            files = l['file_list']
            for file in files:
                if ".md" in file:
                    path = "{}/{}".format(root, file)
                    with open(path, 'rb') as f:
                        lines = f.readlines()
                        markdown_html = self.__parse_markdown__(lines)
                        self.html_content.append({"path": path.replace(".md", ".html"), "content": markdown_html})
        return self

    def get_html(self):
        self.read_markdown()
        return self.html_content

    def __parse_markdown__(self, lines):
        markdown = mistune.Markdown(renderer=self.renderer)
        html_list = []
        for l in lines:
            html_list.append(markdown(l.decode('utf-8')))
        return html_list


class HighlightRenderer(mistune.Renderer):
    def block_quote(self, text):
        return "<div class='blockquote'>{}</div> <br>".format(text)
