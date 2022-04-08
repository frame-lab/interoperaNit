import styled, { css } from "styled-components";

const VARIANTS = {
  default: css`
    border-radius: 30px;
    background-color: ${(props) => props.theme.palette.primary.blue};
  `,
  image: css`
    background-color: transparent;
  `,
};

const TYPES = {
  small: css`
    border: none;
    width: 30px;
    height: 30px;
    ${(props) => props.variant && VARIANTS[props.variant]};
  `,
  large: css`
    border: none;
    height: 50px;
    width: ${(props) => props.width};
    ${(props) => props.variant && VARIANTS[props.variant]};
  `
};

const Button = styled.button`
  ${(props) => TYPES[props.size]};
  ${(props) =>
    props.disabled &&
    css`
      background: #7e8190;
      cursor: not-allowed;
    `};
  outline: none;
  cursor: pointer;
  font-weight: ${(props) => props.theme.typography.button.fontWeight};
  font-size: ${(props) => props.theme.typography.button.fontSize};
  font-family: ${(props) => props.theme.typography.button.fontFamily};
  color: ${(props) => props.color || props.theme.palette.primary.white};
  text-decoration: ${(props) =>
    props.textDecoration || props.theme.typography.button.textDecoration};
`;

export { Button };
