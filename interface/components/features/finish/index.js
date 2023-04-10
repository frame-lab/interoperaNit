import React from "react";
import PropTypes from "prop-types";
import { useRouter } from "next/router";

import Typography from "../../elements/typography";
import Button from "../../elements/button";
import * as Styles from "./styles";

function Finish({ processType, haveQueries, error }) {
  const router = useRouter();
  const processText = () => {
    if (error) return error;

    if (processType === "alignment" && haveQueries) {
      return `Click in the button to download the files.`;
    }
    return `Click in the button to download the file`;
  };

  const downloadFiles = () => {};

  const goToRepeat = () => {
    router.push("repeat");
  };

  return (
    <Styles.Body>
      <Typography fontSize="35px" variant="h1">
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
          <Typography fontSize="20px" width="auto" variant="h1" tAlign="center">
            DOWNLOAD
          </Typography>
        </Button>
      )}
      <Typography fontSize="35px" variant="h1" margin="50px 0 0 0">
        Click in the button below to make new inferences in the aligned data
      </Typography>
      <Button
        onClick={goToRepeat}
        size="large"
        variant="default"
        width="200px"
        margin="20px 0"
      >
        <Typography fontSize="20px" width="auto" variant="h1" tAlign="center">
          REPEAT
        </Typography>
      </Button>
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
