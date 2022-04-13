import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import Typography from "../../elements/typography";
import Radio from "../../elements/radio";
import Button from "../../elements/button";

function Processing({ option, onChange }) {
  const { title, value } = option;

  const changeValue = () => {
    onChange(!value);
  };

  return <></>;
}

Processing.propTypes = {
  option: PropTypes.objectOf(PropTypes.any),
  onChange: PropTypes.func,
};

export default Processing;
