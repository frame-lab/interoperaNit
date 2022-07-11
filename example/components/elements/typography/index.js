import React from "react";
import PropTypes from "prop-types";

import * as S from "./styles";
import { fontScale } from "../../../utils/scale";

function Typography({
  children,
  variant,
  fontSize,
  color,
  FontFamily,
  lineHeight,
  tAlign,
  weight,
  mediaQuery,
  colorMedia,
  margin,
  width,
  height,
  textOverflow,
  whiteSpace,
  overflow,
}) {
  const Element = S.Typographies[variant];
  return (
    <Element
      fontSize={fontScale(fontSize)}
      color={color}
      FontFamily={FontFamily}
      lineHeight={lineHeight}
      tAlign={tAlign}
      weight={weight}
      mediaQuery={mediaQuery}
      colorMedia={colorMedia}
      margin={margin}
      width={width}
      textOverflow={textOverflow}
      height={height}
      whiteSpace={whiteSpace}
      overflow={overflow}
    >
      {children}
    </Element>
  );
}

Typography.propTypes = {
  children: PropTypes.node,
  variant: PropTypes.oneOf([
    "h1",
    "h2",
    "body1",
    "body2",
    "subtitle1",
    "subtitle2",
  ]),
  fontSize: PropTypes.string,
  color: PropTypes.string,
  FontFamily: PropTypes.string,
  lineHeight: PropTypes.string,
  tAlign: PropTypes.string,
  weight: PropTypes.oneOf(["light", "regular", "medium", "bold", "black"]),
  margin: PropTypes.string,
  mediaQuery: PropTypes.string,
  colorMedia: PropTypes.string,
  width: PropTypes.string,
  textOverflow: PropTypes.string,
  height: PropTypes.string,
  whiteSpace: PropTypes.string,
  overflow: PropTypes.string,
};

Typography.defaultProps = {
  children: "",
  variant: "body1",
  fontSize: "",
  color: "#ffffff",
  FontFamily: "sans-serif",
  lineHeight: "",
  tAlign: "left",
  weight: "regular",
  mediaQuery: "",
  colorMedia: "",
  margin: "0",
  width: "auto",
  textOverflow: "clip",
  height: "auto",
  whiteSpace: "normal",
  overflow: "normal",
};

export default Typography;
