import React from "react";
import PropTypes from "prop-types";

import Typography from "../../elements/typography";
import * as Styles from "./styles";

function Process({ process }) {
  const processText = () => {
    switch (process) {
      case "alignment":
        return "alignment";
      case "dm":
        return "deep matcher";
      case "pandas":
        return "query";
    }
  };

  return (
    <Styles.Body>
      <Typography fontSize="35px" variant="h1">
        Realizing the {processText()} process
      </Typography>
    </Styles.Body>
  );
}

Process.propTypes = {
  process: PropTypes.string.isRequired,
};

export default Process;
