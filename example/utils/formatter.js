export function formatRouterPushObject(obj) {
  for (let key in obj) {
    obj[key] = JSON.stringify(obj[key]);
  }
  return obj;
}

export function unformatRouterPushObject(obj) {
  for (let key in obj) {
    obj[key] = JSON.parse(obj[key]);
  }
  return obj;
}
