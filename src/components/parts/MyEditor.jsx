import React, { Component } from "react";
import { EditorState, RichUtils, convertToRaw, convertFromRaw, DefaultDraftBlockRenderMap } from "draft-js";
import Immutable from "immutable";
import Editor from "draft-js-plugins-editor";
import HeadlinesButton from "./toolbar";
import {
  ItalicButton,
  BoldButton,
  UnderlineButton,
  CodeButton,
  UnorderedListButton,
  OrderedListButton,
  BlockquoteButton,
  CodeBlockButton
} from "draft-js-buttons";
import createImagePlugin from "draft-js-image-plugin";
import createInlineToolbarPlugin, {
  Separator
} from "draft-js-inline-toolbar-plugin";
import createMathjaxPlugin from "draft-js-mathjax-plugin";
import $ from "jquery";
import settings from "../settings/settings";
import { markdownToDraft, preprocessMath, draftToMarkdown } from "../markdownToDraft";
import createCodeEditorPlugin from "draft-js-code-editor-plugin";
import "draft-js-inline-toolbar-plugin/lib/plugin.css";
import "draft-js-image-plugin/lib/plugin.css";
import "prismjs/themes/prism-twilight.css";
import MathBlock from "./MathBlock";
//Inline tool bar
const inlineToolbarPlugin = createInlineToolbarPlugin();
const { InlineToolbar } = inlineToolbarPlugin;
const mathjaxPlugin = createMathjaxPlugin(/* optional configuration object */);

const plugins = [
  inlineToolbarPlugin,
  createImagePlugin(),
  createCodeEditorPlugin(),
  mathjaxPlugin
];


export default class CustomEmojiEditor extends Component {
  constructor(props) {
    super(props);
    this.state = {
      editorState: EditorState.createEmpty(),
      mathParts : ""
    };
    this.changeNum = 0;
  }

  componentDidUpdate(prev) {
    if (this.props.download !== prev.download && this.props.download) {
      this.download();
    }
    if (this.props.upload !== prev.upload && this.props.upload) {
      this.upload();
    }

    if (
      this.props.title !== prev.title ||
      this.props.category !== prev.category
    ) {
      if (this.props.title !== "" && this.props.category !== "") {
        $.getJSON(
          settings.getURL("get/post/row"),
          {
            userID: this.props.userID,
            title: this.props.title,
            category: this.props.category
          },
          data => {
            if (data.content === null) {
              return;
            }
            let raw = markdownToDraft(data.content);
            let newEditState = EditorState.createWithContent(
              convertFromRaw(raw)
            );
            this.setState({ editorState: newEditState });
          }
        );
      }
    }
  }

  handleKeyCommand(command, editorState) {
    const newState = RichUtils.handleKeyCommand(editorState, command);
    if (newState) {
      this.onChange(newState);
      return "handled";
    }
    return "not-handled";
  }

  onChange = editorState => {
    this.changeNum += 1;
    if (this.changeNum > 2) {
      this.props.onChange();
    }

    this.setState({
      editorState
    });
  };

  focus = () => {
    this.editor.focus();
  };

  download() {
    let raw = convertToRaw(this.state.editorState.getCurrentContent());
    raw = preprocessMath(raw)
    let markdownString = draftToMarkdown(raw);
    let element = document.createElement("a");
    let file = new Blob(["\ufeff", markdownString], {
      type: "text/plain;charset=utf-8"
    });
    element.href = URL.createObjectURL(file);
    element.download = `Notes.md`;
    element.click();
    this.props.onDownloadEnd();
  }

  upload() {
    let raw = convertToRaw(this.state.editorState.getCurrentContent());
    let markdownString = draftToMarkdown(raw);
    $.post(
      settings.getURL("post/post"),
      {
        userID: this.props.userID,
        title: this.props.title,
        category: this.props.category,
        content: markdownString
      },
      data => {
        console.log(data);
        this.props.onUploadEnd(true);
      }
    ).fail(() => {
      this.props.onUploadEnd(false);
    });
    this.changeNum = 0;
  }

  render() {
    return (
      <div>
        <div className="editor" onClick={this.focus}>
          <Editor
            editorState={this.state.editorState}
            handleKeyCommand={this.handleKeyCommand}
            onChange={this.onChange}
            plugins={plugins}
            ref={element => {
              this.editor = element;
            }}
          />
        </div>
        <div>
          <InlineToolbar>
            {externalProps => (
              <div>
                <BoldButton {...externalProps} />
                <ItalicButton {...externalProps} />
                <UnderlineButton {...externalProps} />
                <CodeButton {...externalProps} />
                <Separator {...externalProps} />
                <br />
                <HeadlinesButton {...externalProps} />
                <UnorderedListButton {...externalProps} />
                <OrderedListButton {...externalProps} />
                <BlockquoteButton {...externalProps} />
                <CodeBlockButton {...externalProps} />
              </div>
            )}
          </InlineToolbar>
        </div>
        {JSON.stringify(this.state.mathParts)}<br></br>
        {JSON.stringify(
          convertToRaw(this.state.editorState.getCurrentContent())
        )}
      </div>
    );
  }
}

