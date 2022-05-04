import React from "react";
import PropTypes from "prop-types";

import Typography from "../../elements/typography";
import * as Styles from "./styles";

function Process({ process_type }) {
  const processText = () => {
    switch (process_type) {
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
  process_type: PropTypes.string.isRequired,
};

export default Process;
