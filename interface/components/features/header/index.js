import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import Typography from "../../elements/typography";

function Header({ headerTitle }) {
  return (
    <Styles.Container>
      <Styles.Header>
        <Typography fontSize="50px" width="auto" tAlign="center" variant="h1">
          {headerTitle}
        </Typography>
        <Styles.MenuItemsContainer>
          <Styles.MenuItem href="validate">Validate</Styles.MenuItem>
          <Styles.MenuItem href="deep_matcher">Deep matcher</Styles.MenuItem>
          <Styles.MenuItem href="queries">Queries</Styles.MenuItem>
        </Styles.MenuItemsContainer>
      </Styles.Header>
    </Styles.Container>
  );
}

Header.propTypes = {
  headerTitle: PropTypes.string,
};

export default Header;
