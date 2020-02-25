import Spacer from "react-add-space";
import React, { Fragment, Component } from "react";
import "../App.css";
import Phone from "../Phone.jsx";
import Contact from "../Contact.jsx";
import uuid from "uuid";

class Add extends Component {
  state = {
    name: "",
    number: ""
  };

  onSubmit = e => {
    e.preventDefault();
    this.props.addcontacts(this.state);
    this.setState({ name: "", number: "" });
  };

  myChangeHandler = event => {
    let nam = event.target.name;
    let val = event.target.value;
    this.setState({ [nam]: val });
  };

  render() {
    return (
      <div className="Add">
        <div class="row">
          <div
            class="col-3 col-s-3 menu"
            style={{ direction: "rtl", font_weight: "bold", font_size: "18px" }}
          ></div>

          <div style={{ direction: "rtl" }} class="col-6 col-s-9">
            <h1>افزودن مخاطب</h1>
            <p>در این بخش به دقت شماره و گروه فرد را وارد کنید</p>
            <div>
              <div class="container">
                <form onSubmit={this.onSubmit} enctype="multipart/form-data">
                  <div class="row">
                    <div class="col-25">
                      <label for="fname">نام</label>
                    </div>
                    <div class="col-75">
                      <input
                        type="text"
                        id="fname"
                        name="name"
                        placeholder="نام مورد نظر ..."
                        onChange={this.myChangeHandler}
                      />
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-25">
                      <label for="lname">شماره تلفن</label>
                    </div>
                    <div class="col-75">
                      <input
                        type="number"
                        id="lname"
                        name="number"
                        placeholder="شماره مورد نظر ..."
                        onChange={this.myChangeHandler}
                      />
                    </div>
                  </div>

                  <div class="row">
                    <div class="col-25">
                      <label for="country">گروه</label>
                    </div>
                    <div class="col-75">
                      <select id="country" name="group"></select>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-25"></div>
                    <div class="col-75"></div>
                  </div>
                  <br />
                  <br />
                  <br />
                  <Spacer amount={8} />
                  <a href="{% url 'add_grp' %}">ساخت گروه جدید </a>
                  <Spacer amount={8} />
                  <a href="{% url 'contacts' %}">برگشت</a>
                  <br />
                  <br />
                  <br />
                  <div class="row">
                    <input type="submit" value="افزودن" className="btn" />
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Add;
