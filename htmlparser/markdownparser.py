from tqdm import tqdm
import os
import mistune


class markdown_parser:
    def __init__(self, file_dict):
        self.html_content = []
        self.file_dict = file_dict

    def read_markdown(self):
        for l in tqdm(self.file_dict):
            root = l['root']
            files = l['file_list']
            for file in files:
                if ".md" in file:
                    path = os.path.join(root, file)
                    with open(path, 'rb') as f:
                        lines = f.readlines()
                        markdown = self.__parse_markdown__(lines)
                        self.html_content.append({"path": path.replace(".md", ".html"), "content": markdown})

    @staticmethod
    def __parse_markdown__(lines):
        markdown = mistune.Markdown()
        html_list = []
        for l in lines:
            html_list.append(markdown(l.decode('utf-8')))
        return html_list
