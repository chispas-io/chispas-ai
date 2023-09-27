// TODO: use vite config to set baseUrl
const baseUrl = "http://localhost:5000/api/";

const defaultHeaders = {
  "Content-Type": "multipart/form-data",
};

const defaultOptions = {
  method: "GET",
  headers: defaultHeaders,
};

export const jinxFetch = (url, options = {}, headers={}) => {
  return fetch(baseUrl + url, {
    ...defaultOptions,
    ...options,
  })
    .catch(err => console.log(err));
}
