import styled from "styled-components";

export const Image = styled.div`
  width: ${(props) => props.width};
  height: ${(props) => props.height};
  max-height: ${(props) => props.maxHeight};
  background-image: url(${(props) => props.image});
  background-repeat: ${(props) => props.repeat};
  background-color: ${(props) => props.color};
  background-position: ${(props) => props.position};
  background-size: ${(props) => props.size};
  filter: ${(props) => props.filter};
`;
