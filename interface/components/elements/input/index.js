import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";

function Input(
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
    <Styles.Input
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

Input.propTypes = {
  type: PropTypes.string,
  value: PropTypes.string.isRequired,
  color: PropTypes.string,
  background: PropTypes.string,
  border: PropTypes.string,
  borderRadius: PropTypes.string,
  width: PropTypes.string,
  height: PropTypes.string,
  onChange: PropTypes.func.isRequired,
  props: PropTypes.oneOf([PropTypes.string]),
};

Input.defaultProps = {
  type: "text",
  color: "black",
  background: "white",
  border: "transparent",
  borderRadius: "10px",
  width: "80%",
  height: "30px",
  props: {},
};

export default Input;
