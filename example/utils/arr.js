export function Add(getter, setter, obj) {
  const arrCopy = [...getter, obj];
  setter(arrCopy);
}

export function Remove(getter, setter, index) {
  const arrCopy = [...getter];
  arrCopy.splice(index, 1);
  setter(arrCopy);
}

export function Change(getter, setter, obj, index) {
  const arrCopy = [...getter];
  arrCopy[index] = obj;
  setter(arrCopy);
}
