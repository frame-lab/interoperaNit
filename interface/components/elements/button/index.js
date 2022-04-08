import React from "react";
import PropTypes from "prop-types";

import * as S from "./styles";

const Button = ({
  children,
  variant,
  onClick,
  disabled,
  type,
  size,
  color,
  textDecoration,
  margin,
  width,
}) => {
  return (
    <S.Button
      variant={variant}
      onClick={onClick}
      disabled={disabled}
      type={type}
      size={size}
      color={color}
      textDecoration={textDecoration}
      margin={margin}
      width={width}
    >
      {children}
    </S.Button>
  );
};

Button.propTypes = {
  children: PropTypes.node,
  onClick: PropTypes.func,
  size: PropTypes.oneOf(["small", "large"]),
  variant: PropTypes.oneOf(["default", "image"]),
  disabled: PropTypes.bool,
  type: PropTypes.string,
  color: PropTypes.string,
  textDecoration: PropTypes.string,
  margin: PropTypes.string,
  width: PropTypes.string,
};

Button.defaultProps = {
  children: "",
  onClick: () => {},
  size: "small",
  variant: "default",
  disabled: false,
  type: "button",
  color: "",
  textDecoration: "",
  margin: "0",
  width: "auto",
};

export default Button;
