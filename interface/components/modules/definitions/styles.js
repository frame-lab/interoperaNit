import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  height: 500px;
  width: 100%;
  align-items: center;
  margin-top: 30px;
  margin-bottom: 30px;
`;

export const HorizontalContainer = styled.div`
  display: flex;
  flex-direction: row;
  margin-top: 20px;
  justify-content: space-around;
  width: ${(props) => props.width};
  flex-wrap: wrap
`;
