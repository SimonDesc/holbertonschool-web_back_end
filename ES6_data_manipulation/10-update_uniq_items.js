export default function updateUniqueItems(newMap) {
  if (newMap instanceof (Map)) {
    newMap.forEach((valeur, clé) => {
      if (valeur === 1) {
        newMap.set(clé, 100);
      }
    });
  } else {
    throw new Error('Cannot process');
  }
}
