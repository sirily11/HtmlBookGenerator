import React, { Component } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import language from '../settings/language';


export default class Header extends Component {
  render() {
    return (
      <div className="row header">
        <h2 className="ml-auto mr-auto my-auto">{language.notes}</h2>
      </div>
    )
  }
}
