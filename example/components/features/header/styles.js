import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  width: 100%;
  justify-content: center;
`;

export const Header = styled.div`
  display: flex;
  flex-direction: row;
  height: 70px;
  width: 80%;
  align-items: center;
  background-color: #063970;
  border-bottom-left-radius: 100px;
  border-bottom-right-radius: 100px;
  padding-left: 50px;
`;

export const MenuItemsContainer = styled.div`
  display: flex;
  width: 100%;
  align-items: center;
  justify-content: space-around;
  background-color: transparent;
  padding-left: 100px;
  padding-right: 100px;
`;

export const MenuItem = styled.a`
  font-size: ${(props) => props.fontSize};
  color: white;
  text-decoration: none;
  background-color: transparent;
  transition: all 0.3s ease-out;
  position: relative;
`;
