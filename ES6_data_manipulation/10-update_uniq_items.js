export default function updateUniqueItems(map) {
  if (map instanceof Map) {
    map.forEach((valeur, cle) => {
      if (valeur === 1) {
        map.set(cle, 100);
      }
    });
    return map;
  }

  throw new Error('Cannot process');
}
