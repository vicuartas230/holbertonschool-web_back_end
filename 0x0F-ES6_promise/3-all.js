import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  uploadPhoto()
    .then((res) => {
      createUser()
        .then((resp) => {
          console.log(res.body, resp.firstName, resp.lastName);
        })
        .catch(() => {
          console.log('Signup system offline');
        });
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
