import React from "react";
import PropTypes from "prop-types";

import { CreateFiles } from "../../../utils/file";
import * as Styles from "./styles";

function Processing({ path, files, alternative, options }) {
  return <Styles.Container></Styles.Container>;
}

Processing.propTypes = {
  path: PropTypes.string.isRequired,
  files: PropTypes.arrayOf(PropTypes.any).isRequired,
  alternative: PropTypes.bool,
  options: PropTypes.arrayOf(PropTypes.string),
};

Processing.defaultProps = {
  alternative: false,
  options: [],
};

export default Processing;
