export default function getResponseFromAPI () {
  return new Promise((resolve, reject) => {
    // Simulating an asynchronous API call
    setTimeout(() => {
      const response = { status: 200, body: 'Success' };
      resolve(response);
    }, 1000);
  });
}
