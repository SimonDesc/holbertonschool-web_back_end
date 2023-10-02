export default function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);

  return Promise.allSettled([userPromise, photoPromise])
    .then((results) => {
      const transformedResults = [];

      for (let i = 0; i < results.length; i++) {
        let value;
        if (results[i].status === 'fulfilled') {
          value = results[i].value;
        } else {
          value = results[i].reason.toString();
        }

        transformedResults.push({
          status: results[i].status,
          value,
        });
      }

      return transformedResults;
    });
}
