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
        {definitionList.map((definition, index) => {
          const definitionKey = `definition_${index}`;

          return <DefinitionItem definition={definition} key={definitionKey} />;
        })}
      </Styles.HorizontalContainer>
      <Styles.HorizontalContainer width="50%">
        {options.map((option, index) => {
          const onChange = (value) => Change(options, setOptions, value, index);

          const optionKey = `option_${index}`;

          return (
            <OptionItem option={option} onChange={onChange} key={optionKey} />
          );
        })}
      </Styles.HorizontalContainer>
    </Styles.Container>
  );
}

Definitions.propTypes = {
  definitionList: PropTypes.shape([]).isRequired,
  options: PropTypes.shape([]).isRequired,
  setOptions: PropTypes.func.isRequired,
};

export default Definitions;
