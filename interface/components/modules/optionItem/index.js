import React, { useState } from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import Typography from "../../elements/typography";
import Radio from "../../elements/radio";
import Button from "../../elements/button";
import Input from "../../elements/input";

function OptionItem({ option, onChange }) {
  const { title, value, percent } = option;

  const changeValue = () => {
    onChange({ ...option, value: !value });
  };

  const changePercent = (event) => {
    onChange({ ...option, percent: event.target.value });
  };

  const havePercent = () => {
    if (percent !== undefined) {
      return <Input value={percent} onChange={changePercent} width='50px'/>;
    }
    return null;
  };

  return (
    <Styles.Container>
      <Button onClick={changeValue} size="large" variant="image">
        <Styles.HorizontalContainer>
          <Radio value={value} onChange={onChange} />
          <Typography
            margin="0 0 0 10px"
            fontSize="20px"
            width="150px"
            variant="h1"
          >
            {title}
          </Typography>
        </Styles.HorizontalContainer>
      </Button>
      {havePercent()}
    </Styles.Container>
  );
}

OptionItem.propTypes = {
  option: PropTypes.objectOf(PropTypes.any).isRequired,
  onChange: PropTypes.func.isRequired,
};

export default OptionItem;
