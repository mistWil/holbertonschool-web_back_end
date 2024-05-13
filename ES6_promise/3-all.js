import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup () {
  return Promise.all([uploadPhoto(), createUser()])
    .then((values) => {
      const [photoData, userData] = values;
      console.log(`${photoData.body} ${userData.firstName} ${userData.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
