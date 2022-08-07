export default function uploadPhoto(filename) {
  const promise = new Promise((reject) => {
    reject(`${filename} cannot be processed`);
  });
  return promise;
}
