import React, { Component } from 'react';
import './App.css';
import MyEditor from './components/parts/MyEditor';
import Home from './components/container/Home';

class App extends Component {
  render() {
    return (
      <div>
        <Home></Home>
      </div>
    );
  }
}

export default App;
