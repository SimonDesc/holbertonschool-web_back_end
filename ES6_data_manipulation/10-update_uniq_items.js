export default function updateUniqueItems(newMap) {
  // console.log(newMap)
  newMap.forEach((valeur, clé) => {
    if (valeur === 1) {
      newMap.set(clé, 100);
    }
  });
}
