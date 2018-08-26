from flask import Flask, request, redirect, url_for, flash
from flask import render_template
from htmlparser.markdownparser import Markdown, HighlightRenderer
from htmlparser.htmlGenerator import HTMLGenerator
import json
import os

app = Flask(__name__)
cust_renderer = HighlightRenderer()
test_dir = "pages/text"


@app.route("/")
def home():
    markdown = Markdown(test_dir, renderer=cust_renderer)
    dir_dict = markdown.generate_dir_dict()
    return render_template("home.html", folders=dir_dict)


@app.route("/get_content")
def get_content():
    markdown = Markdown(test_dir, renderer=cust_renderer)
    file_name = request.args.get("file_name")
    folder = request.args.get("folder")
    path = "{}/{}".format(folder, file_name).replace("md", "html")
    contents = markdown.get_html()
    for i, content in enumerate(contents):
        if path in content['path']:
            return json.dumps(content['content'])
    return ""


@app.route("/save", methods=["POST", "GET"])
def save():
    markdown = Markdown(test_dir, renderer=cust_renderer)
    if request.method == 'POST':
        markdown_content = json.loads(request.form['markdown'])["content"]
        file_name = request.form['file_name']
        folder = request.form['folder']
        print(markdown)

        with open("{}/{}/{}".format(test_dir, folder, file_name), 'wb') as f:
            for l in markdown_content:
                f.write("{}\n".format(l).encode("utf-8"))
            f.close()
            print("Saved")
    return json.dumps({"success": True})


@app.route("/create_folder", methods=["POST"])
def create_folder():
    if request.method == 'POST':
        folder = "{}/{}".format(test_dir, request.form['folder'])
        if not os.path.exists(folder):
            os.makedirs(folder)
    return json.dumps({"success": True})


@app.route("/create_file", methods=["POST"])
def create_file():
    if request.method == 'POST':
        file = request.form['file_name'].split(".")
        path = "{}/{}/{}.{}".format(test_dir, request.form['folder'], file[0], file[1].lower())
        open(path, "w+")

    return json.dumps({"success": True})


@app.route("/publish", methods=["POST"])
def publish():
    if request.method == 'POST':
        markdown = Markdown(file_dir=test_dir,renderer=cust_renderer)
        html = HTMLGenerator(markdown_parser=markdown)
        html.output_HTML(color_selection="#d84315").output_indexHTML()
        print("Converted")
    return json.dumps({"success": True})


if __name__ == '__main__':
    pages_folder = os.path.exists("pages/text")
    static_folder = os.path.exists("static")
    template_folder = os.path.exists("templates")

    if static_folder and template_folder:
        print("read to edit")
        print("For windows user, please go to http://localhost:8080 instead")
        app.run(host='0.0.0.0', port=8080)
    else:
        print("Copy everything from the zip to this folder")
        input("Press any key to exit")

