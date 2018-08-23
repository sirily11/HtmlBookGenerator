import os
import mistune
from tqdm import tqdm

class HTMLGenerator:
    def __init__(self, videodir, captiondir):
        self.video_dir = videodir
        self.caption_dir = captiondir
        self.dir_dict = self.__generate_dir_dict__()
        self.html_content = []

    def read_markdown(self):
        for l in tqdm(self.dir_dict):
            root = l['root']
            files = l['file_list']
            for file in files:
                if ".md" in file:
                    path = os.path.join(root, file)
                    with open(path, 'rb') as f:
                        lines = f.readlines()
                        markdown = self.__parse_markdown__(lines)
                        self.html_content.append({"path": path.replace(".md", ".html"), "content": markdown})

    def output_HTML(self, color="#bdbdbd"):
        for h in self.html_content:
            with open(h['path'], 'wb') as f:
                content = ""
                title = os.path.basename(h['path']).replace(".html", "")
                nav = self.__generate_menu__(title, color)
                if h['content']:
                    for l in h['content']:
                        content += l

                # print(content)
                f.write(self.__html_tenplate__(title, content=content, nav=nav).encode('utf8'))

    @staticmethod
    def __parse_markdown__(lines):
        markdown = mistune.Markdown()
        html_list = []
        for l in lines:
            html_list.append(markdown(l.decode('utf-8')))
        return html_list

    def __generate_dir_dict__(self):
        dir_dict = []
        for root, dirs, files in os.walk(self.video_dir, topdown=False):
            if len(files) != 0:
                dir_dict.append({
                    "root": root,
                    "folder_name": os.path.basename(root),
                    "file_list": files
                })
        return dir_dict

    def __html_tenplate__(self, name, nav, content):
        return """
        <!DOCTYPE html>
        <head>
            <meta charset="UTF-8">
            <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0'>
            <script src="../../../assets/scripts/core/jquery.min.js"></script>
            <script src="../../../assets/scripts/core/popper.min.js"></script>
            <script src="../../../assets/scripts/bootstrap-material-design.js"></script>
            <script src="../../../assets/scripts/material-kit.js?v=2.0.0"></script>
            <link rel="stylesheet" href="../../../assets/stylesheet/material-kit.css">
            <link rel="stylesheet" href="../../../assets/stylesheet/style.css">
            <link rel="stylesheet" type="text/css"
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Roboto+Slab:400,700|Material+Icons"/>
            <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
            <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
            <title>{}</title>
        </head>
        <body>
        <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
        {}
          <main class="mdl-layout__content">
          {}
          </main>
        </div>
        </body>
        </html>
          
        """.format(name, nav, content)

    def __generate_menu__(self, title, color):
        card_title = ""
        card_content = ""
        card = ""
        for folder in self.dir_dict:
            file_list = ""
            card_title += """
                <div class="card-header" role="tab" id="heading{}">
                    <h5 class="mb-0">
                        <a data-toggle="collapse" href="#collapse{}" aria-expanded="false" aria-controls="collapse{}">
                            {}
                            <i class="material-icons">keyboard_arrow_down</i>
                        </a>
                    </h5>
                </div>
            """.format(folder['folder_name'], folder['folder_name'], folder['folder_name'], folder['folder_name'])
            for file in folder['file_list']:
                if "html" in file:
                    # side bar menu
                    file_list += """
                                <ul class="list-group">
                                    <li class="list-group-item">
                                       <a href="{}"> {} </a>
                                    </li>
                                </ul>
                                    """.format("""..\{}\{}""".format(folder['folder_name'], file),
                                               file.replace(".html", ""))
            card_content += """
                    <div id="collapse{}" class="collapse" role="tabpanel" aria-labelledby="heading{}"
                     data-parent="#accordion">
                        {}
                     </div>
            """.format(folder['folder_name'], folder['folder_name'], file_list)

            card += """
             <div class="card card-collapse">
             {}
             {}
             </div>
            """.format(card_title, card_content)
            card_title = ""
            card_content = ""

        return """
          <header class="mdl-layout__header" style="background-color:{}">
            <div class="mdl-layout__header-row">
              <span class="mdl-layout-title">{}</span>
              <div class="mdl-layout-spacer"></div>
            </div>
          </header>
          <div class="mdl-layout__drawer">
            <span class="mdl-layout-title">Title</span>
            <nav class="mdl-navigation">
                   <div id="accordion" role="tablist">
                        {}
                    </div>
            </nav>
          </div>

        """.format(color, title, card)


if "speechtotext" not in os.path.basename(os.getcwd()):
    print("You should put this file in the doc file")

color = input("Color theme[in hex]: ")
print("Start the html conversion")
text_dir = "pages/text"
html = HTMLGenerator(text_dir, "")
html.read_markdown()
if len(color) > 3:
    html.output_HTML(color)
else:
    html.output_HTML()
print("Finished")
input("Press any key to quit")
