import React from "react";

import * as Styles from "./styles";
import Typography from "../../elements/typography";
import Image from "../../elements/image";
import { useWindowDimensions } from "../../../utils/window";
import { fontScale } from "../../../utils/scale";

function Header() {
  const { width, height } = useWindowDimensions();

  const icuff =
    process.env.NODE_ENV === "production"
      ? `${process.env.BACKEND_URL}/icuff.png`
      : "icuff.png";

  const linkFont = `${fontScale(width, height, 20)}px`;

  return (
    <Styles.Container>
      <Styles.Header>
        <Image
          image={icuff}
          width="170px"
          height="60px"
          size="cover"
          alt="iduff"
        />
        <Typography fontSize={30} width="auto" tAlign="center" variant="h1">
          Interopera
        </Typography>
        <Styles.MenuItemsContainer>
          <Styles.MenuItem
            href={`${process.env.BACKEND_URL}/`}
            fontSize={linkFont}
          >
            ALIGNMENT
          </Styles.MenuItem>
          <Styles.MenuItem
            href={`${process.env.BACKEND_URL}/postprocessing`}
            fontSize={linkFont}
          >
            POST PROCESSING
          </Styles.MenuItem>
        </Styles.MenuItemsContainer>
      </Styles.Header>
    </Styles.Container>
  );
}

export default Header;
