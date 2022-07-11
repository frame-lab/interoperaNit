import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";

function Textarea(
  {
    type,
    value,
    color,
    background,
    border,
    borderRadius,
    width,
    height,
    onChange,
  },
  props
) {
  return (
    <Styles.Textarea
      type={type}
      value={value}
      color={color}
      background={background}
      border={border}
      borderRadius={borderRadius}
      width={width}
      height={height}
      onChange={onChange}
      {...props}
    />
  );
}

Textarea.propTypes = {
  type: PropTypes.string,
  value: PropTypes.string.isRequired,
  color: PropTypes.string,
  background: PropTypes.string,
  border: PropTypes.string,
  borderRadius: PropTypes.string,
  width: PropTypes.string,
  height: PropTypes.string,
  onChange: PropTypes.func.isRequired,
  props: PropTypes.shape({}),
};

Textarea.defaultProps = {
  type: "text",
  color: "black",
  background: "white",
  border: "transparent",
  borderRadius: "5px",
  width: "80%",
  height: "100px",
  props: {},
};

export default Textarea;
