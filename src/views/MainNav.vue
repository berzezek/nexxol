<template lang="">
  <div>
    <!-- Navigation-->
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
      <div class="container px-4 px-lg-5" v-if="$route.path === '/'">
        <a class="navbar-brand" @click="$router.push('/')"><img class="navbar-logo-img" src="@/assets/img/logo.png"
            style="width: 150px" alt="NEXXOL" /></a>
        <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse"
          data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false"
          aria-label="Toggle navigation">
          Меню
          <i class="fas fa-bars"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item"><a class="nav-link" href="#about">О нас</a></li>
            <li class="nav-item"><a class="nav-link" href="#projects">Проекты</a></li>
            <li class="nav-item"><a class="nav-link" @click="$router.push('/products')">Продукты</a></li>
            <li class="nav-item"><a class="nav-link" href="#signup">Контакты</a></li>
          </ul>
        </div>
      </div>
      <div class="container px-4 px-lg-5" v-else>
        <a class="navbar-brand" @click="$router.push('/')"><img class="navbar-logo-img" src="@/assets/img/logo.png"
            style="width: 150px" alt="NEXXOL" /></a>
        
      </div>
    </nav>
  </div>
</template>
<script>

</script>

<style lang="">
  /* @import '@/css/styles.css' */
</style>