import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import Image from "../image";

function Radio({ value }) {
  const check =
    process.env.NODE_ENV === "production"
      ? `${process.env.BACKEND_URL}/done.svg`
      : "done.svg";

  return (
    <Styles.Container>
      {value && (
        <Image
          image={check}
          width="30px"
          height="30px"
          size="cover"
          alt="check"
        />
      )}
    </Styles.Container>
  );
}

Radio.propTypes = {
  value: PropTypes.bool.isRequired,
};

export default Radio;
