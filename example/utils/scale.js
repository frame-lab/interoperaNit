export const normalize = (width, height, size, based = "width") => {
  const widthScale = width / 1920;
  const heightScale = height / 1080;
  const newSize = based === "height" ? size * heightScale : size * widthScale;
  return Math.round(newSize);
};

export const fontScale = (width, height, size, factor = 0.5) => {
  return size + (normalize(width, height, size) - size) * factor;
};
