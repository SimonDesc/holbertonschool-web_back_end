import { createUser, uploadPhoto } from './utils';

export default function handleProfileSignup() {
  const promises = [uploadPhoto(), createUser()];

  Promise.all(promises)
    .then(([photoResult, userResult]) => {
      console.log(photoResult.body, userResult.firstName, userResult.lastName);
    })
    .catch((error) => {
      console.error('Signup system offline', error);
    });
}
