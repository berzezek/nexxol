<template>
  <div class="container">
    <form @submit.prevent>
      <div class="mb-3">
        <label class="form-label">Login</label>
        <input type="text" class="form-control" v-model="loginData.username" />
      </div>
      <div class="mb-3">
        <label class="form-label">Password</label>
        <input
          type="password"
          class="form-control"
          v-model="loginData.password"
        />
      </div>
      <button class="btn btn-primary" @click="loginPost">Submit</button>
    </form>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      loginData: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    async loginPost() {
      console.log('ok')
      await axios.post(`auth/token/login/`, this.loginData)
        .then(response => {
          this.loginData.username = '';
          this.loginData.password = '';
          if (response.status === 200) {
            this.$toast.success('Успешно')
            localStorage.setItem('token', response.data.auth_token);

          } else {
            this.$toast.error('Что-то пошло не так :(')
          }
        })
        // .then(() => {
        //   router.push("/dashboard-view");
        // })
    }
  },
};
</script>
<style>

</style>