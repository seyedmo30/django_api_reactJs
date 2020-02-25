import Spacer from "react-add-space";
import "./App.css";

import uuid from "uuid";
import React, { Component } from "react";
class Phone extends Component {
  state = {};
  getStyleName = () => {
    if (this.props.contacts.ss) {
      return { color: "red" };
    } else {
      return { color: "blue" };
    }
  };

  render() {
    return (
      <div class="div1">
        <div style={{ float: "left", direction: "ltr", border: "0px" }}>
          <img
            class="photo"
            src="default.jpg"
            alt="rate"
            width="70"
            height="60"
          />
        </div>

        <div class="div2" style={this.getStyleName()}>
          {this.props.contacts.name}
          <Spacer amount={8} />
          {this.props.contacts.number}
          <Spacer amount={8} />
          <div style={{ float: "left" }}>
            <button
              onClick={this.props.delContact.bind(this, this.props.contacts.id)}
            >
              <img
                class="star"
                src="delete.png"
                alt="rate"
                width="40"
                height="auto"
              />
            </button>
            <Spacer amount={8} />
            <a href="{{contact.get_absolute_url}}">
              <img
                class="star"
                src="edit.png"
                alt="rate"
                width="40"
                height="auto"
              />
            </a>
            <Spacer amount={8} />
          </div>
        </div>
      </div>
    );
  }
}

export default Phone;
