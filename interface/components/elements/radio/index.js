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
  option: PropTypes.objectOf(PropTypes.any),
};

export default Radio;
