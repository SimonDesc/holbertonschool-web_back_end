export default function hasValuesFromArray(Set, Array) {
  const setToArray = [...Set];

  const sortedArray1 = Array.sort();
  const sortedArray2 = setToArray.sort();

  for (let i = 0; i < sortedArray1.length; i += 1) {
    if (sortedArray1[i] !== sortedArray2[i]) {
      return false;
    }
  }
  return true;
}
