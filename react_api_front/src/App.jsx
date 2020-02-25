import Spacer from "react-add-space";
import React, { Fragment, Component } from "react";
import Index from "./pages/Index.jsx";
import Add from "./pages/Add.jsx";
import "./App.css";

import { API_URL } from "./constants.jsx";

import Phone from "./Phone.jsx";
import Contact from "./Contact.jsx";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useRouteMatch,
  useParams
} from "react-router-dom";

import uuid from "uuid";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.searchcontact = this.searchcontact.bind(this);
    this.state = {
      search_value: "",
      contacts: [],

    };
  }
  componentDidMount() {
    axios.get(API_URL).then(res => this.setState({ contacts: res.data }));

  }


  componentDidUpdate(prevState) {

  }

  delContact = idd => {

    axios.delete('http://localhost:8000/api/' + idd + '/delete/')
      .then(res => this.setState({
        contacts: this.state.contacts.
          filter(del => this.state.contacts.id !== idd)
      }))

  };

  searchcontact = text => {
    this.setState({ search_value: text.target.value })
    axios.get('http://localhost:8000/api/search/?search=' + text.target.value).then((response) => {
      this.setState({ contacts: response.data })
    })
  };

  addcontacts = newcontact => {
    axios.post("http://localhost:8000/api/create/",
      {
        name: newcontact.name,
        number: newcontact.number,
        group: 1,
        user: 1,
      }).then(res => this.setState({ contacts: [...this.state.contacts, res.data] }))

  };

  render() {
    return (
      <div className="App">
        <Router>
          <div class="topnav" id="myTopnav">
            <Link to="/" class="active">
              Home
            </Link>

            <Link to="/add">LogIn</Link>

            <a href="javascript:void(0);" class="icon" onclick="myFunction()">
              <i class="fa fa-bars"></i>
            </a>
          </div>
          <Switch>
            <Route
              exact
              path="/"
              render={contacts => (
                <Index
                  contacts={this.state.contacts}
                  delContact={this.delContact}
                />
              )}
            />
            <Route
              exact
              path="/add"
              render={addcontacts => <Add addcontacts={this.addcontacts} />}
            />
          </Switch>
        </Router>
        <div class="col-3 col-s-12">
          <div class="aside">
            <h2>برترین فیلم ها؟</h2>
            <p>می توانید برترین فیلم ها از دیدگاه مردم را مشاهده کنید</p>

            <br />
            <h2>برترین آهنگ های ماندگار؟</h2>
            <p>
              <input type="text" name="text" value={this.state.search_value} onChange={this.searchcontact} />
              ماندگار ترین موسیقی های سه خواننده، ابی ، داریوش و هایده را گوش
              دهید
            </p>
            <br />
            <h2>ارتباط با ما</h2>
            <p>
              می توانید انتقادات و پیشنهادات خود را از طریق ایمیل زیر به ما
              ارسال کنید
              <br />
              <br />
              seyedmo30@gmail.com
            </p>
          </div>
        </div>

        <div class="footer">
          <p>
            Resize the browser window to see how the content respond to the
            resizing.
          </p>
        </div>
      </div>
    );
  }
}

export default App;
