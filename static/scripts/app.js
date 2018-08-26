var folder = "";
var file_name = "";

$("button").click(function (e) {
    document.execCommand($(this).attr("id"));
});

$("#quote").click(function (e) {
    var text = window.getSelection().getRangeAt(0).toString();

    var html = `<h3 class='blockquote' style="font-size: 20px;">${text}</h3>`;
    document.execCommand("insertHTML", true, html);
    document.execCommand('insertParagraph', false);
});

$(".heading").click(function (e) {
    var text = window.getSelection().getRangeAt(0).toString();
    switch ($(this).html()) {
        case "Heading 1":
            addHeading(1, text);
            break;
        case "Heading 2":
            addHeading(2, text);
            break;
        case "Heading 3":
            addHeading(3, text);
            break;
        case "Heading 4":
            addHeading(4, text);
            break;
        case "Heading 5":
            addHeading(5, text);
            break;
        case "Heading 6":
            addHeading(6, text);
            break;
    }
});

$("#bulleted").click(function (e) {
    var text = $('.edit-area').editableContent().toString().split("<br>");
    var html = "";
    var list = "";
    for (var i = 0; i < text.length; i++) {
        list += `<li><p>${text[i]}</p></li>`
    }
    html = `<ul style="list-style-type:disc">${list}</ul>`;
    document.execCommand("insertHTML", true, html);
    document.execCommand('insertParagraph', false);
    document.execCommand("delete", false, null);
});

$('.dropdown').bind("mousedown", function (e) {
    e.preventDefault();
});


$("#content").keypress(function (e) {
    var keycode = (event.keyCode ? event.keyCode : event.which);
    console.log("saved");
    if (keycode === 13) {
        $.post("/save",
            {
                "markdown": JSON.stringify(htmlToMarkdown()),
                "folder": folder.toString(),
                "file_name": file_name.toString()
            })
    }
});

function htmlToMarkdown() {
    const turndownService = new TurndownService();
    var content = $('#content').html().split("<div>");
    var list = [];
    for (var i = 0; i < content.length; i++) {
        console.log(content[i].split("</div>")[0]);
        var line = content[i].split("</div>")[0];
        var markdown = turndownService.turndown(`${line}`);
        if (line.includes("blockquote")) {
            markdown = `> ${markdown}`;
        }

        list.push(markdown);
    }
    return {"content": list};
}

function addHeading(heading, content) {
    var html = `<h${heading}>${content}</h${heading}>`;
    document.execCommand("insertHTML", true, html);
    document.execCommand('insertParagraph', false);
}
