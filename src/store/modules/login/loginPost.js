// import router from '@/router/router'
import axios from 'axios';
export default {
  actions: {
    async getLogin(ctx, loginData) {
      await axios.post(`auth/token/login/`, loginData)
        .then(response => {
          if (response.status === 200) {
            this.$toast.success('Успешно!')
            localStorage.setItem('token', response.data.auth_token);
            router.push("/dashboard-view");
          } else {
            this.$toast.alert('Произошла ошибка!')
          }
        })
    }
  },
  mutations: {},
  getters: {},
  state: {}
}