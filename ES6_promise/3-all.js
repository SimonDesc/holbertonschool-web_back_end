import { createUser, uploadPhoto } from './utils';

export default function handleProfileSignup() {
  const promises = [uploadPhoto(), createUser()];
  Promise.all(promises)
    .then((result) => {
      console.log(result[0].body, result[1].firstName, result[1].lastName);
    })
    .catch(() => {
      console.error('Signup system offline');
    });
}
