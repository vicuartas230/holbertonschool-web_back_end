import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((res) => ({
      status: res[0].status,
      value: res[0].value,
    }))
    .catch((err) => ({
      status: err[1].status,
      value: err[1].reason,
    }));
}
