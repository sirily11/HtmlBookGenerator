import os
from htmlparser.elements import Div, H1, H2, Main, Body, H5, A, I, Ul, Li
from htmlparser.markdownparser import Markdown


class HTMLGenerator:
    def __init__(self, markdown_parser: Markdown):
        self.markdown_parser = markdown_parser
        self.dir_dict = markdown_parser.generate_dir_dict()
        self.html_content = markdown_parser.get_html()

    def output_HTML(self, color_selection="#bdbdbd"):
        for h in self.html_content:
            with open(h['path'], 'wb') as f:
                content = ""
                title = os.path.basename(h['path']).replace(".html", "")
                nav = self.__generate_menu__(title, color_selection)
                if h['content']:
                    for l in h['content']:
                        content += l

                f.write(self.__html_tenplate__(title, content=content, nav=nav).encode('utf8'))
        return self

    def output_indexHTML(self):
        filename = str(self.dir_dict[0]['file_list'][0])
        if ".md" in filename:
            filename.replace("md","html")
        html = Div({"class": "container h-100"}).add(
            Div({"class": "row h-100 justify-content-center align-items-center"})).add(
            A({"href": "text/{}/{}".format(self.dir_dict[0]["folder_name"],filename),
               "style": "font-size:30px"},
              contents="Read")).toString()

        template = """
         <!DOCTYPE html>
        <head>
        <link rel="stylesheet" href="../static/stylesheet/material-kit.css">
        </head>
        <body>""" + html + "</body></html>"

        with open("pages/index.html", "wb") as f:
            f.write(template.encode("utf-8"))

    def __html_tenplate__(self, name, nav, content):
        return """
        <!DOCTYPE html>
        <head>
            <meta charset="UTF-8">
            <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0'>
            <script src="../../../static/scripts/core/jquery.min.js"></script>
            <script src="../../../static/scripts/core/popper.min.js"></script>
            <script src="../../../static/scripts/bootstrap-material-design.js"></script>
            <script src="../../../static/scripts/material-kit.js?v=2.0.0"></script>
            <link rel="stylesheet" href="../../../static/stylesheet/material-kit.css">
            <link rel="stylesheet" href="../../../static/stylesheet/style.css">
            <link rel="stylesheet" type="text/css"
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Roboto+Slab:400,700|Material+Icons"/>
            <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
            <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
            <title>{}</title>
            </head>
            <body>
                {}
            </body>
            </html>
          
        """.format(name, Div({"class": "mdl-layout mdl-js-layout mdl-layout--fixed-header"}, nav)
                   .add(Main({"class": "mdl-layout__content"}, content)).toString())

    def __generate_menu__(self, title, color):
        card_title = ""
        card_content = ""
        card = ""
        for folder in self.dir_dict:
            file_list = ""
            card_title += Div({"class": "card-header",
                               "role": "tab",
                               "id": "heading{}".format(folder['folder_name'])}) \
                .add(H5({"class": "mb-0"})) \
                .add(A({"data-toggle": "collapse",
                        "href": "#collapse{}".format(folder['folder_name']),
                        "aria-expanded": "false",
                        "aria-controls": "collapse{}".format(folder['folder_name'])},
                       contents=folder['folder_name'])
                     .add(I({"class": "material-icons"}, contents="keyboard_arrow_down"))) \
                .toString()

            for file in folder['file_list']:
                if "html" in file:
                    # side bar menu
                    file_list += Ul({"class": "list-group"}) \
                        .add(Li({"class": "list-group-item"})) \
                        .add(A({"href": """..\{}\{}""".format(folder['folder_name'], file)},
                               contents=file.replace(".html", ""))) \
                        .toString()
            card_content += Div({"id": "collapse{}".format(folder['folder_name']),
                                 "class": "collapse{} collapse".format(folder['folder_name']),
                                 "role": "tabpanel",
                                 "aria-labelledby": "heading{}".format(folder['folder_name']),
                                 "data-parent": "#according"}, contents=file_list).toString()

            card += Div({"class": "card card-collapse"}, "{}\n{}".format(card_title, card_content)).toString()
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
