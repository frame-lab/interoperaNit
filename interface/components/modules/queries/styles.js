import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  height: 500px;
  width: 70%;
  margin-top: 30px;
`;

export const Scroll = styled.div`
  display: flex;
  flex-direction: column;
  overflow-y: scroll;
  ::-webkit-scrollbar {
    display: none;
  }
`;

export const HorizontalContainer = styled.div`
  display: flex;
  flex-direction: row;
  margin-top: 20px;
  justify-content: space-around;
`;
