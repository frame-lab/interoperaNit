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
    width: 10px;
  }
  ::-webkit-scrollbar-track {
    box-shadow: inset 0 0 5px grey;
    border-radius: 10px;
  }
  ::-webkit-scrollbar-thumb {
    background: grey;
    border-radius: 10px;
  }
`;

export const HorizontalContainer = styled.div`
  display: flex;
  flex-direction: row;
  margin-top: 20px;
  justify-content: space-around;
`;
