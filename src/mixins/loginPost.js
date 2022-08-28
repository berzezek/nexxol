import axios from 'axios';
export default {
  methods: {
    async getLogin(loginData) {
      console.log('ok')
      await axios.post(`auth/token/login/`, loginData)
        .then(response => {
          if (response.status === 200) {
            alert('Success')
            localStorage.setItem('token', response.data.auth_token);
          } else {
            alert('Something wrong')
          }
        })
        // .then(() => {
        //   router.push("/dashboard-view");
        // })
    }
  },

}