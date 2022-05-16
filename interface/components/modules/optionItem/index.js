import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import Typography from "../../elements/typography";
import Radio from "../../elements/radio";
import Button from "../../elements/button";

function OptionItem({ option, onChange }) {
  const { title, value, code } = option;

  const changeValue = () => {
    onChange({ title, value: !value, code });
  };

  return (
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
  );
}

OptionItem.propTypes = {
  option: PropTypes.objectOf(PropTypes.any).isRequired,
  onChange: PropTypes.func.isRequired,
};

export default OptionItem;
