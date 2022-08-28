<script>
import MainNav from '@/views/MainNav.vue'
import MainFooter from '@/views/MainFooter.vue'
export default {
  components: {
    MainNav,
    MainFooter
  }
}
</script>

<template>
  <div>
    <main-nav v-if="$route.path !== '/dashboard'"/>
      <router-view></router-view>
    <main-footer v-if="$route.path !== '/dashboard'"/>
  </div>
</template>

<style scoped>

</style>
