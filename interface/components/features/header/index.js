import React from "react";

import * as Styles from "./styles";
import Typography from "../../elements/typography";

function Header() {
  return (
    <Styles.Container>
      <Styles.Header>
        <Typography fontSize="50px" width="auto" tAlign="center" variant="h1">
          Interopera
        </Typography>
        <Styles.MenuItemsContainer>
          <Styles.MenuItem href="\">ALIGNMENT</Styles.MenuItem>
          <Styles.MenuItem href="options">OPTIONS</Styles.MenuItem>
        </Styles.MenuItemsContainer>
      </Styles.Header>
    </Styles.Container>
  );
}

export default Header;
