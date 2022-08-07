function signUpUser(firstName, lastName) {
  const promise = new Promise((resolve) => {
    resolve({
      firstName,
      lastName,
    });
  });
  return promise;
}

module.exports = signUpUser;
