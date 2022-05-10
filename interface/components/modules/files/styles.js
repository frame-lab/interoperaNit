import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  height: 480px;
  width: 70%;
  margin-top: 30px;
  align-items: center;
  margin-bottom: 30px;
`;

export const HorizontalContainer = styled.div`
  display: flex;
  flex-direction: row;
  margin-top: 30px;
`;

export const DragArea = styled.div`
  display: flex;
  flex-direction: column;
  height: 400px;
  width: 70%;
  border: 5px dashed white;
  border-radius: 50px;
  align-items: center;
  justify-content: center;
`;

export const VerticalContainer = styled.div`
  display: flex;
  flex-direction: column;
  margin-top: 30px;
  margin-left: 50px;
`;

export const Scroll = styled.div`
  display: flex;
  flex-direction: column;
  height: 300px;
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
  border: 5px solid white;
  border-radius: 20px;
`;
