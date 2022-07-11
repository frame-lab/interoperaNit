import React from "react";
import PropTypes from "prop-types";

import Finish from "../components/features/finish";

export default function Finished({ processType, haveQueries }) {
  return <Finish processType={processType} haveQueries={haveQueries} />;
}

Finished.propTypes = {
  processType: PropTypes.string,
  haveQueries: PropTypes.bool,
};

Finished.defaultProps = {
  processType: null,
  haveQueries: null,
};
