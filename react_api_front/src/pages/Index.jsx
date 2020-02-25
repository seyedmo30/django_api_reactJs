import Spacer from "react-add-space";
import React, { Fragment, Component } from "react";
import "../App.css";
import Phone from "../Phone.jsx";
import Contact from "../Contact.jsx";
import uuid from "uuid";

class Index extends Component {
  state = {};
  render() {
    return (
      <div className="Index" style={{ direction: "rtl" }}>
        <div class="row">
          <div class="col-3 col-s-3 menu">
            <form action="{% url 'post_search' %}" method="get">
              <input type="submit" value="salam" />
            </form>

            <ul>
              <a href="/contacts">
                <li>all </li>
              </a>

              <a href="{{group.get_absolute_url }}">
                <li>دانشگاه </li>
              </a>
              <a href="{{group.get_absolute_url }}">
                <li>دانشگاه </li>
              </a>
            </ul>

            <div class="col-6 col-s-3 menu">
              <a href="/add_grp">
                <li> add group </li>
              </a>
            </div>
            <div class="col-6 col-s-3 menu">
              <a href="/add_grp">
                <li> drop group </li>
              </a>
            </div>
          </div>
        </div>

        <div style={{ direction: "rtl" }} class="col-6 col-s-9">
          <h1>خوش آمدید</h1>

          <p>
            در این سایت شما می توانید شماره تلفن و ایمیل مورد نظر را ذخیره کنید.
          </p>
          <div style={{ margin: "10px" }}>
            <a href="{% url 'add'%}">
              <div
                class="div1"
                style={{
                  background_color: "pink ",
                  text_align: " center",
                  font_size: "40px"
                }}
              >
                <b>افزودن + </b>
              </div>
            </a>

            <Contact
              contacts={this.props.contacts}
              delContact={this.props.delContact}
            />
          </div>
        </div>
      </div>
    );
  }
}

export default Index;
