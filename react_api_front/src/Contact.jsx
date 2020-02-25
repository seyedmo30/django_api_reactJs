import React, { Fragment, Component } from "react";
import Phone from "./Phone";
import PropType from "prop-types";
class Contact extends Component {
  render() {
    return this.props.contacts.map(contacts => (
      <Phone
        contacts={contacts}
        key={contacts.id}
        delContact={this.props.delContact}
      />
    ));
  }
}

Contact.PropType = {
  contacts: PropType.object.isRequired
};

export default Contact;
