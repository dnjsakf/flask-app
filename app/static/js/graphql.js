// Create Axios Instance for HTTP   
var gql = axios.create({
    method: "post",
    baseURL: '/graphql',
    timeout: 5*1000,
    headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
});
