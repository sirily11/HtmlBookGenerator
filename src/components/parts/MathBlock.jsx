import React, { Component } from "react";
import MathJax from "react-mathjax2";

export default class MathBlock extends Component {
  constructor(props) {
    super(props);
    this.state = { renderMath: false };
  }

  componentWillMount() {}

  renderMath() {
    return this.props.blockProps.math.map((m, i) => {
      return (
        <MathJax.Node key={i} inline>
          {m.replace(/\$/g, "")}
        </MathJax.Node>
      );
    });
  }

  render() {
    return (
      <div>
        <MathJax.Context input="ascii">
          <div>{this.props.blockProps && this.renderMath()}</div>
        </MathJax.Context>
      </div>
    );
  }
}
