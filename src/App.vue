<script>
import MainNav from '@/views/MainNav.vue'
import MainFooter from '@/views/MainFooter.vue'
export default {
  components: {
    MainNav,
    MainFooter
  },
  computed: {
    doNotShowInDashboard() {
      let path = this.$route.path.search(/dashboard/)
      return (true ? path !== 1 : false)
    }
  }
}
</script>

<template>
  <div>
    <main-nav v-if="doNotShowInDashboard"/>
      <router-view></router-view>
    <main-footer v-if="doNotShowInDashboard"/>
  </div>
</template>

<style>

</style>
