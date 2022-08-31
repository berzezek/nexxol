<template>
  <div>
    <div v-if="currIsAuthenticate" class="">
      <main-dashboard :user="currUser"></main-dashboard>
    </div>

    <div v-else class="dashboard">
      <main-login></main-login>
    </div>
  </div>
</template>
<script>
import MainLogin from "@/components/login/MainLogin.vue";
import MainDashboard from "@/views/MainDashboard.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  components: {
    MainLogin,
    MainDashboard,
  },
  methods: {
    ...mapActions({
      loginGet: "loginGet/getUser",
    }),
  },
  computed: {
    ...mapGetters({
      currUser: "loginGet/currUser",
      currIsAuthenticate: "loginGet/currIsAuthenticate",
    }),
  },
  mounted() {
    this.loginGet();
  },
};
</script>
<style>
.dashboard {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>