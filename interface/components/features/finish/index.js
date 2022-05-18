import React from "react";
import PropTypes from "prop-types";

import Typography from "../../elements/typography";
import * as Styles from "./styles";

function Finish({ processType, haveQueries, error }) {
  const processText = () => {
    if (error) return error;

    const textToShow = `Your files are ready in `;

    switch (processType) {
      case "alignment":
        const QueryText = haveQueries
          ? " and your queries can be found in /interopera/result"
          : "";
        return textToShow + "/interopera/csv" + QueryText;
      case "dm":
        return textToShow + "/interopera/csv";
      case "pandas":
        return textToShow + "/interopera/result";
    }
  };

  return (
    <Styles.Body>
      <Typography fontSize="35px" variant="h1">
        {processText()}
      </Typography>
    </Styles.Body>
  );
}

Finish.propTypes = {
  processType: PropTypes.string,
  haveQueries: PropTypes.bool,
  error: PropTypes.string,
};

Finish.defaultProps = {
  processType: null,
  haveQueries: null,
  error: null,
};

export default Finish;
