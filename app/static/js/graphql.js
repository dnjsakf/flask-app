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

var getUserList = function(){
    return gql({
        data: {
            query: `{
                userList {
                    email
                    name
                }
            }`
        }
    });
}

var userList = getUserList();


async function test(){
    var data = gql({
        data: {
            query: `{
                userList {
                    email
                    name
                }
            }`
        }
    }).then(await function(resp){
       return resp.data; 
    });
    return data;
}
