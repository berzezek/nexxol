import axios from "axios";
import router from '@/router/'
export default {
  state: () => ({
    username: '',
    isAuthenticate: false
  }),
  actions: {
    async getUser(ctx) {
      let username = '';
      let isAuthenticate;
      await axios.get(`auth/users/me/`, {
          headers: {
            'Authorization': `Token ${localStorage.token}`
          }
        })
        .then(response => {
          if (response.status === 200) {
            username = response.data.username;
            isAuthenticate = true;
          }
        })
        .catch(e => {
          if (e.response.status === 401) {
            router.push('/dashboard')
          }
        })


      ctx.commit('updateUsername', username)
      ctx.commit('updateIsAuthenticate', isAuthenticate)
    }
  },
  mutations: {
    updateUsername(state, username) {
      state.username = username
    },
    updateIsAuthenticate(state, isAuthenticate) {
      state.isAuthenticate = isAuthenticate
    }
  },
  getters: {
    currUser(state) {
      return state.username
    },
    currIsAuthenticate(state) {
      return state.isAuthenticate
    }
  },
  namespaced: true
}