import React from "react";

import * as Styles from "./styles";
import Typography from "../../elements/typography";
import Image from "../../elements/image";

function Header() {
  const icuff =
    process.env.NODE_ENV === "production"
      ? `${process.env.BACKEND_URL}/icuff.png`
      : "icuff.png";

  return (
    <Styles.Container>
      <Styles.Header>
        <Image
          image={icuff}
          width="170px"
          height="60px"
          size="cover"
          alt="icuff"
        />
        <Typography fontSize="50px" width="auto" tAlign="center" variant="h1">
          Interopera
        </Typography>
        <Styles.MenuItemsContainer>
          <Styles.MenuItem href={`${process.env.BACKEND_URL}/`}>
            ALIGNMENT
          </Styles.MenuItem>
          <Styles.MenuItem href={`${process.env.BACKEND_URL}/postprocessing`}>
            POST PROCESSING
          </Styles.MenuItem>
        </Styles.MenuItemsContainer>
      </Styles.Header>
    </Styles.Container>
  );
}

export default Header;
