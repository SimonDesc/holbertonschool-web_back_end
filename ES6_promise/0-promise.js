// Return a Promise using this prototype function getResponseFromAPI()

export default function getResponseFromAPI() {
  return new Promise((resolve) => {
    resolve('La promesse est résolue');
  });
}
