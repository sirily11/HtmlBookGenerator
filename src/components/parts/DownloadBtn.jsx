import React, { Component } from 'react'
import CloudDownloadIcon from "@material-ui/icons/CloudDownload";
import { IconButton, Menu, MenuItem } from "@material-ui/core";
export default class DownloadBtn extends Component {
  render() {
    return (
      <div>
        <IconButton onClick={()=>{this.props.download()}}><CloudDownloadIcon></CloudDownloadIcon></IconButton>
      </div>
    )
  }
}
