import React from "react";
import PropTypes from "prop-types";

import Typography from "../../elements/typography";
import Button from "../../elements/button";
import * as Styles from "./styles";

function Finish({ processType, haveQueries, error }) {
  const processText = () => {
    if (error) return error;

    if (processType === "alignment" && haveQueries) {
      return `Click in the button to download the files.`;
    }
    return `Click in the button to download the file`;
  };

  const downloadFiles = () => {};

  return (
    <Styles.Body>
      <Typography fontSize={35} variant="h1">
        {processText()}
      </Typography>
      {!error && (
        <Button
          onClick={downloadFiles}
          size="large"
          variant="default"
          width="200px"
          margin="20px 0"
        >
          <Typography fontSize={20} width="auto" variant="h1" tAlign="center">
            DOWNLOAD
          </Typography>
        </Button>
      )}
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
