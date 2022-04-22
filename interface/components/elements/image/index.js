import React from "react";
import PropTypes from "prop-types";

import * as S from "./styles";

const Image = ({
  image,
  width,
  height,
  maxHeight,
  repeat,
  color,
  position,
  size,
  filter,
}) => {
  return (
    <S.Image
      image={image}
      width={width}
      height={height}
      maxHeight={maxHeight}
      repeat={repeat}
      color={color}
      position={position}
      size={size}
      filter={filter}
    />
  );
};

Image.propTypes = {
  image: PropTypes.string.isRequired,
  width: PropTypes.string,
  height: PropTypes.string,
  maxHeight: PropTypes.string,
  repeat: PropTypes.string,
  color: PropTypes.string,
  position: PropTypes.string,
  size: PropTypes.string,
  filter: PropTypes.string,
};

Image.defaultProps = {
  width: "100%",
  height: "100%",
  repeat: "no-repeat",
  color: "transparent",
  position: "center",
  size: "auto",
  filter: "",
  maxHeight: "none",
};

export default Image;
