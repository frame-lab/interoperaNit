import useWindowDimensions from "./window";

export const normalize = (size, based = "width") => {
  const widthScale = useWindowDimensions.width / 375;
  const heightScale = useWindowDimensions.height / 667;

  const newSize = based === "height" ? size * heightScale : size * widthScale;
  return Math.round(newSize);
};

export const fontScale = (size, factor = 0.5) =>
  size + (normalize(size) - size) * factor;
