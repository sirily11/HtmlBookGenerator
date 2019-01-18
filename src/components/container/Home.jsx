import React, { Component } from "react";
import MyEditor from "../parts/MyEditor";
import Header from "../parts/Header";
import "bootstrap/dist/css/bootstrap.min.css";
import DownloadBtn from "../parts/DownloadBtn";
import UploadBtn from "../parts/UploadBtn";
import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import ExpansionPanelSummary from "@material-ui/core/ExpansionPanelSummary";
import ExpansionPanelDetails from "@material-ui/core/ExpansionPanelDetails";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import { Typography, Select, MenuItem } from "@material-ui/core";
import AddPhotoAlternate from "@material-ui/icons/AddPhotoAlternate";
import $ from "jquery";
import settings from "../settings/settings";
import language from "../settings/language";
import TitleField from "../parts/TitleField";

export default class Home extends Component {
  constructor() {
    super();
    this.state = {
      download: false,
      upload: false,
      title: "",
      categories: [],
      titles: [],
      category: "",
      saveStatus: "Not save"
    };
    this.userID = "";
  }

  componentWillMount() {
    $.getJSON(settings.getURL("get/category"), data => {
      this.userID = data.uid;
      this.setState({ categories: data.category, titles: data.title });
    });
  }

  editor = () => {
    return (
      <div style={{ width: "100%" }}>
        <Header />
        <div className="row" style={{ marginLeft: 50 }}>
          <DownloadBtn
            download={() => {
              this.setState({ download: true });
            }}
          />
          <UploadBtn
            upload={() => {
              this.setState({ upload: true });
            }}
          />
          <div className="ml-4 my-auto">{this.state.saveStatus}</div>
        </div>
        <MyEditor
          userID={this.userID}
          title={this.state.title}
          category={this.state.category}
          upload={this.state.upload}
          onChange={() => {
            this.setState({ saveStatus: "Not save" });
          }}
          onUploadEnd={success => {
            this.setState({
              upload: false,
              saveStatus: success ? "Saved" : "Fail to save"
            });
          }}
          download={this.state.download}
          onDownloadEnd={() => {
            this.setState({ download: false });
          }}
        />
      </div>
    );
  };

  renderSelection() {
    return this.state.categories.map((category, i) => {
      return (
        <MenuItem key={i} value={category}>
          {category}
        </MenuItem>
      );
    });
  }

  render() {
    return (
      <div className="container-fluid">
        <TitleField
          title={this.state.title}
          titles={this.state.titles}
          onChange={newTitle => {
            this.setState({ title: newTitle });
          }}
        />
        <ExpansionPanel>
          <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
            <Typography>
              {language.category}: {this.state.category}
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Select
              onChange={e => {
                this.setState({ category: e.target.value });
              }}
              value={this.state.category}
              style={{ width: 150 }}
            >
              {this.renderSelection()}
            </Select>
          </ExpansionPanelDetails>
        </ExpansionPanel>
        {this.editor()}
      </div>
    );
  }
}
