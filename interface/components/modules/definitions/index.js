import React from "react";
import PropTypes from "prop-types";

import * as Styles from "./styles";
import DefinitionItem from "../definitionItem";
import OptionItem from "../optionItem";
import { Change } from "../../../utils/arr";

function Definitions({ definitionList, options, setOptions }) {
  return (
    <Styles.Container>
      <Styles.HorizontalContainer width="80%">
        {definitionList.map((definition, index) => (
          <DefinitionItem definition={definition} key={index} />
        ))}
      </Styles.HorizontalContainer>
      <Styles.HorizontalContainer width="50%">
        {options.map((option, index) => {
          const onChange = (value) => Change(options, setOptions, value, index);

          return <OptionItem option={option} onChange={onChange} key={index} />;
        })}
      </Styles.HorizontalContainer>
    </Styles.Container>
  );
}

Definitions.propTypes = {
  definitionList: PropTypes.arrayOf(PropTypes.any).isRequired,
  options: PropTypes.arrayOf(PropTypes.any).isRequired,
  setOptions: PropTypes.func.isRequired,
};

export default Definitions;
