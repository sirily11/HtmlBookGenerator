import React, { Component } from 'react'
import CloudUploadIcon from "@material-ui/icons/CloudUpload";
import { IconButton, Menu, MenuItem } from "@material-ui/core";
export default class UploadBtn extends Component {
  render() {
    return (
      <div>
        <IconButton onClick={()=>{this.props.upload()}}><CloudUploadIcon></CloudUploadIcon></IconButton>
      </div>
    )
  }
}
