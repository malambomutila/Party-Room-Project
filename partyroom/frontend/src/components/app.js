import React, { Component } from "react";
import { createRoot } from 'react-dom/client';
// import HomePage from "./HomePage";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <HomePage />
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
root.render(<App />, appDiv);