import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import Image from "../../elements/image";

function Radio({ value }) {
  const check = "done.svg";

  return (
    <Styles.Container>
        {value && (
          <Image image={check} width="30px" height="30px" size="cover" />
        )}
    </Styles.Container>
  );
}

Radio.propTypes = {
  value: PropTypes.bool.isRequired,
};

export default Radio;
