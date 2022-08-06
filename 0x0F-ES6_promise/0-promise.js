function getResponseFromAPI() {
    const promise = new Promise((resolve, reject) => {
        resolve(1);
    });
    return promise;
}

export { getResponseFromAPI as default };
