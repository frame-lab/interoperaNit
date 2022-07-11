import styled from "styled-components";

const h1 = styled.h1`
  font-size: ${(props) => props.fontSize || props.theme.typography.h1.fontSize};
  color: ${(props) => props.color || props.theme.palette.text.default};
  font-family: ${(props) => props.FontFamily};
  font-weight: ${(props) =>
    `${props.theme.typography.fontWeight[props.weight]}`};
  line-height: ${(props) =>
    props.lineHeight || props.theme.typography.h1.lineHeight};
  text-align: ${(props) => props.tAlign || props.theme.typography.h1.tAlign};
  margin: ${(props) => props.margin};
  ${(props) => props.width && `width: ${props.width}`};
  text-overflow: ${(props) => props.textOverflow};
  height: ${(props) => props.height};
  white-space: ${(props) => props.whiteSpace};
  overflow: ${(props) => props.overflow};
  background-color: transparent;

  @media (${(props) => props.mediaQuery}) {
    color: ${(props) => props.colorMedia};
  }
`;

const h2 = styled.h2`
  font-size: ${(props) => props.fontSize || props.theme.typography.h2.fontSize};
  color: ${(props) => props.color || props.theme.palette.text.default};
  font-family: ${(props) => props.FontFamily};
  font-weight: ${(props) =>
    `${props.theme.typography.fontWeight[props.weight]}`};
  line-height: ${(props) =>
    props.lineHeight || props.theme.typography.h2.lineHeight};
  text-align: ${(props) => props.tAlign || props.theme.typography.h2.tAlign};
  margin: ${(props) => props.margin};
  ${(props) => props.width && `width: ${props.width}`};
  text-overflow: ${(props) => props.textOverflow};
  height: ${(props) => props.height};
  white-space: ${(props) => props.whiteSpace};
  overflow: ${(props) => props.overflow};
  background-color: transparent;

  @media (${(props) => props.mediaQuery}) {
    color: ${(props) => props.colorMedia};
  }
`;

const body1 = styled.p`
  font-size: ${(props) =>
    props.fontSize || props.theme.typography.body1.fontSize};
  color: ${(props) => props.color || props.theme.palette.text.default};
  font-family: ${(props) => props.FontFamily};
  font-weight: ${(props) =>
    `${props.theme.typography.fontWeight[props.weight]}`};
  line-height: ${(props) =>
    props.lineHeight || props.theme.typography.body1.lineHeight};
  text-align: ${(props) => props.tAlign || props.theme.typography.body1.tAlign};
  margin: ${(props) => props.margin};
  ${(props) => props.width && `width: ${props.width}`};
  text-overflow: ${(props) => props.textOverflow};
  height: ${(props) => props.height};
  white-space: ${(props) => props.whiteSpace};
  overflow: ${(props) => props.overflow};
  background-color: transparent;

  @media (${(props) => props.mediaQuery}) {
    color: ${(props) => props.colorMedia};
  }
`;

const body2 = styled.p`
  font-size: ${(props) =>
    props.fontSize || props.theme.typography.body2.fontSize};
  color: ${(props) => props.color || props.theme.palette.text.default};
  font-family: ${(props) => props.FontFamily};
  font-weight: ${(props) =>
    `${props.theme.typography.fontWeight[props.weight]}`};
  line-height: ${(props) =>
    props.lineHeight || props.theme.typography.body2.lineHeight};
  text-align: ${(props) => props.tAlign || props.theme.typography.body2.tAlign};
  margin: ${(props) => props.margin};
  ${(props) => props.width && `width: ${props.width}`};
  text-overflow: ${(props) => props.textOverflow};
  height: ${(props) => props.height};
  white-space: ${(props) => props.whiteSpace};
  overflow: ${(props) => props.overflow};
  background-color: transparent;

  @media (${(props) => props.mediaQuery}) {
    color: ${(props) => props.colorMedia};
  }
`;

const subtitle1 = styled.p`
  font-size: ${(props) =>
    props.fontSize || props.theme.typography.subtitle1.fontSize};
  color: ${(props) => props.color || props.theme.palette.text.default};
  font-family: ${(props) => props.FontFamily};
  font-weight: ${(props) =>
    `${props.theme.typography.fontWeight[props.weight]}`};
  line-height: ${(props) =>
    props.lineHeight || props.theme.typography.subtitle1.lineHeight};
  text-align: ${(props) =>
    props.tAlign || props.theme.typography.subtitle1.tAlign};
  margin: ${(props) => props.margin};
  ${(props) => props.width && `width: ${props.width}`};
  text-overflow: ${(props) => props.textOverflow};
  height: ${(props) => props.height};
  white-space: ${(props) => props.whiteSpace};
  overflow: ${(props) => props.overflow};
  background-color: transparent;

  @media (${(props) => props.mediaQuery}) {
    color: ${(props) => props.colorMedia};
  }
`;

const subtitle2 = styled.p`
  font-size: ${(props) =>
    props.fontSize || props.theme.typography.subtitle2.fontSize};
  color: ${(props) => props.color || props.theme.palette.text.default};
  font-family: ${(props) => props.FontFamily};
  font-weight: ${(props) =>
    `${props.theme.typography.fontWeight[props.weight]}`};
  line-height: ${(props) =>
    props.lineHeight || props.theme.typography.subtitle2.lineHeight};
  text-align: ${(props) =>
    props.tAlign || props.theme.typography.subtitle2.tAlign};
  margin: ${(props) => props.margin};
  ${(props) => props.width && `width: ${props.width}`};
  text-overflow: ${(props) => props.textOverflow};
  height: ${(props) => props.height};
  white-space: ${(props) => props.whiteSpace};
  overflow: ${(props) => props.overflow};
  background-color: transparent;

  @media (${(props) => props.mediaQuery}) {
    color: ${(props) => props.colorMedia};
  }
`;

const Typographies = {
  h1,
  h2,
  body1,
  body2,
  subtitle1,
  subtitle2,
};

export { Typographies };
