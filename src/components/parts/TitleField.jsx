import React, { Component } from "react";
import language from "../settings/language";
import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import ExpansionPanelSummary from "@material-ui/core/ExpansionPanelSummary";
import ExpansionPanelDetails from "@material-ui/core/ExpansionPanelDetails";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import { Typography, TextField, Paper, MenuItem } from "@material-ui/core";
import Popper from "@material-ui/core/Popper";

const getSuggestions = (titles, value) => {
  const inputValue = value.trim().toLowerCase();
  const inputLength = inputValue.length;

  return inputLength === 0
    ? []
    : titles.filter(
        lang => lang.toLowerCase().slice(0, inputLength) === inputValue
      );
};

export default class TitleField extends Component {
  constructor() {
    super();
    this.state = {
      value: "",
      suggestions: [],
      anchorEl: null
    };
  }

  onSuggestionsFetchRequested = value => {
    this.setState({
      suggestions: getSuggestions(this.props.titles, value)
    });
  };

  onSuggestionsClearRequested = () => {
    this.setState({
      suggestions: []
    });
  };

  renderSuggestions() {
    return this.state.suggestions.map((suggestion, i) => {
      return (
        <MenuItem
          key={`sugges-${i}`}
          onClick={() => {
            this.onSuggestionsClearRequested()
            this.props.onChange(suggestion);
            
          }}
        >
          {suggestion}
        </MenuItem>
      );
    });
  }
  render() {
    return (
      <div>
        <ExpansionPanel>
          <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
            <Typography>
              {language.title}: {this.props.title}
            </Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <TextField
              value={this.props.title}
              onChange={e => {
                this.onSuggestionsFetchRequested(e.target.value);
                this.setState({ anchorEl: e.currentTarget });
                this.props.onChange(e.target.value);
              }}
              fullWidth
            />
            <Popper
              id="0"
              open={this.state.suggestions.length !== 0}
              anchorEl={this.state.anchorEl}
              placement="bottom-start"
              style={{ zIndex: 1 }}
              transition
            >
              <Paper>{this.renderSuggestions()}</Paper>
            </Popper>
          </ExpansionPanelDetails>
        </ExpansionPanel>
      </div>
    );
  }
}
