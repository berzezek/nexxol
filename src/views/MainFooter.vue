<template lang="">
  <div>
    <!-- Contact-->
    <section class="contact-section bg-black">
      <div class="container px-4 px-lg-5">
        <div class="row gx-4 gx-lg-5">

          <div class="col-md-4 mb-3 mb-md-0">
            <a href="https://goo.gl/maps/K6k9y483rRAtxNs37" target="_blank" class="text-decoration-none">
              <div class="card py-4 h-100">
                <div class="card-body text-center">
                  <i class="fas fa-map-marked-alt text-primary mb-2"></i>
                  <h4 class="text-uppercase m-0">Наш адрес</h4>
                  <hr class="my-4 mx-auto" />
                  <div class="small text-black-50">Республика Узбекистан, г.Ташкент, Юнусабадский район, массив Киет 56А
                  </div>
                </div>
              </div>
            </a>
          </div>
          <div class="col-md-4 mb-3 mb-md-0">
            <a href="mailto:info@b-oil.uz" target="_blank" class="text-decoration-none">
              <div class="card py-4 h-100">
                <div class="card-body text-center">
                  <i class="fas fa-envelope text-primary mb-2"></i>
                  <h4 class="text-uppercase m-0">E-mail</h4>
                  <hr class="my-4 mx-auto" />
                  <div class="small text-black-50"><a href="#!">o.fahritdinova@yandex.ru</a></div>
                </div>
              </div>
            </a>
          </div>
          <div class="col-md-4 mb-3 mb-md-0">
            <div class="card py-4 h-100">
              <a href="tel:+998954100300" class="text-decoration-none">
                <div class="card-body text-center">
                  <i class="fas fa-mobile-alt text-primary mb-2"></i>
                  <h4 class="text-uppercase m-0">Телефон</h4>
                  <hr class="my-4 mx-auto" />
                  <div class="small text-black-50">+998 (95) 410-0300
                  </div>
                </div>
              </a>
            </div>
          </div>
        </div>
        <!-- <div class="social d-flex justify-content-center">
                    <a class="mx-2" href="#!"><i class="fab fa-twitter"></i></a>
                    <a class="mx-2" href="#!"><i class="fab fa-facebook-f"></i></a>
                    <a class="mx-2" href="#!"><i class="fab fa-github"></i></a>
                </div> -->
      </div>
    </section>
    <!-- Footer-->
    <footer class="footer bg-black small text-center text-white-50">
      <div class="container px-4 px-lg-5">Copyright <span @click="$router.push({name: 'dashboard'})">&copy;</span> <img class="footer-logo" src="@/assets/img/logo-white.png"
            style="width: 75px" alt="NEXXOL"/> 2022</div>
    </footer>
  </div>
</template>
<script>
export default {};
</script>
<style >
  .my-bg {
    background-image: url('@/assets/img/secondary-bg.webp');
    background-size: cover;
  }
  /* @import '@/css/styles.css' */
</style>