export default function cleanSet(Set, startString) {
  let stringAllSet = '';

  if (typeof startString !== 'string') {
    return stringAllSet;
  }

  if (startString === '') {
    return stringAllSet;
  }

  const strLenght = startString.length;

  for (const value of Set) {
    if (value.search(startString) !== -1) {
      const startStr = value.search(startString); // position de début
      stringAllSet += value.substring(startStr + strLenght);
      stringAllSet += '-';
    }
  }

  stringAllSet = stringAllSet.slice(0, -1);

  return stringAllSet;
}
