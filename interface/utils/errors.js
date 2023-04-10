export const verifyToolErrors = (error) => {
  if (
    error.message.includes("pandas.core.computation.ops.UndefinedVariableError")
  ) {
    return "Please revise your queries and try again.";
  }
  return "";
};
