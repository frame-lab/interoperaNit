import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  height: 270px;
  width: 250px;
`;

export const Scroll = styled.div`
  margin-top: 15px;
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
