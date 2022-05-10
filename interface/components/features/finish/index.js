import React from "react";
import PropTypes from "prop-types";

import Typography from "../../elements/typography";
import * as Styles from "./styles";

function Finish({ processType, haveQueries }) {
  const processText = () => {
    switch (processType) {
      case "alignment":
        const QueryText = haveQueries
          ? " and your queries can be found in /interopera/result"
          : "";
        return "/interopera/csv" + QueryText;
      case "dm":
        return "/interopera/csv";
      case "pandas":
        return "/interopera/result";
    }
  };

  return (
    <Styles.Body>
      <Typography fontSize="35px" variant="h1">
        Your files are ready in {processText()}
      </Typography>
    </Styles.Body>
  );
}

Finish.propTypes = {
  processType: PropTypes.string.isRequired,
  haveQueries: PropTypes.bool.isRequired,
};

export default Finish;
