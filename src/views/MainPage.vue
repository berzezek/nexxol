<template>
  <div>
    <!-- Masthead-->
    <header class="masthead">
      <div
        class="
          container
          px-4 px-lg-5
          d-flex
          h-100
          align-items-center
          justify-content-center
        "
      >
        <div class="d-flex justify-content-center">
          <div class="text-center">
            <h1 class="mx-auto my-0 text-uppercase">
              engine <br />
              oil <br />
              industrial
            </h1>
            <h3 class="text-white-50 mx-auto mt-5 display-6">
              Моторные масла в Узбекистане.
            </h3>
            <!-- <a class="btn btn-primary" href="#about">Get Started</a> -->
          </div>
        </div>
      </div>
    </header>
    <!-- About-->
    <section class="about-section" id="about">
      <div class="container px-4 px-lg-5">
        <div class="row gx-4 gx-lg-5 justify-content-center">
          <div class="col-lg-8">
            <h2 class="text-white mb-4 text-uppercase">
              engine oil industrial
            </h2>
            <p class="text-white-50">
              Использует базовые масла высокой очистки и европейские присадки,
              что позволяет оснащать продукцию Viraj лучшими международными
              характеристиками, оставаясь при этом доступными по цене. Мы
              предлагаем только самую качественную продукцию и даем ответы на
              сложные технические вопросы.
            </p>
          </div>
        </div>
        <div class="d-flex justify-content-center">
          <img
            class="img-fluid mb-5 d-flex justify-content-center"
            src="../assets/img/xx.png"
            alt="NEXXOL"
          />
        </div>
      </div>
    </section>
    <!-- Projects-->
    <section class="projects-section bg-light" id="projects">
      <div class="container px-4 px-lg-5">
        <!-- Featured Project Row-->
        <div class="row gx-0 mb-4 mb-lg-5 align-items-center">
          <div class="col-xl-8 col-lg-7">
            <img
              class="img-fluid mb-3 mb-lg-0"
              src="../assets/img/oil-shop.webp"
              alt="Oil Shop"
            />
          </div>
          <div class="col-xl-4 col-lg-5">
            <div class="featured-text text-lg-left">
              <h4 class="text-uppercase">Наша продукция</h4>
              <p class="text-black-50 mb-0 text-left">
                Продукция, которая гарантирует качество и уход за двигателем.
                <br /><br />Моторные масла семейства VIRAJ имеют формулу,
                идеально соответствующую потребностям вашего автомобиля.
                <br /><br />Ознакомьтесь с нашим широким ассортиментом, чтобы
                найти лучшее моторное масло для вашего автомобиля.<br /><br />

                Одним из приоритетов
                <span class="text-uppercase">engine oil industrial</span>
                является постоянный контроль и улучшение, поэтому продукция
                систематически проходит программу лабораторных исследований
                STANDART SERVICE FOREVER.
              </p>
            </div>
          </div>
        </div>
        <!-- Project One Row-->
        <div class="row gx-0 mb-5 mb-lg-0 justify-content-center">
          <div class="col-lg-6 image-container" v-if="!product_1.image_1">
            <img
              class="image-center"
              :src="product_1.get_thumbnail"
              :alt="product_1.name"
            />
          </div>
          <div class="col-lg-6 image-container" v-else>
            <img
              class="image-center"
              :src="product_1.image_1"
              :alt="product_1.name"
            />
          </div>
          <div class="col-lg-6">
            <div class="bg-black h-100 project">
              <div class="d-flex h-100">
                <div class="project-text w-100 my-auto text-lg-left">
                  <h4 class="text-white">{{ product_1.name }}</h4>
                  <p class="mb-0 text-white-50">{{ product_1.description }}</p>
                  <hr class="d-none d-lg-block mb-1 ms-0" />
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Project Two Row-->
        <div class="row gx-0 justify-content-center">
          <div class="col-lg-6">
            <div class="bg-black h-100 project">
              <div class="d-flex h-100">
                <div class="project-text w-100 my-auto text-lg-left">
                  <h4 class="text-white">{{ product_2.name }}</h4>
                  <p class="mb-0 text-white-50">{{ product_2.description }}</p>
                  <hr class="d-none d-lg-block mb-1 ms-0" />
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-6 image-container" v-if="!product_2.image_1">
            <img
              class="image-center"
              :src="product_2.get_thumbnail"
              :alt="product_2.name"
            />
          </div>
          <div class="col-lg-6 image-container" v-else>
            <img
              class="image-center"
              :src="product_2.image_1"
              :alt="product_2.name"
            />
          </div>
        </div>
      </div>
      <div class="d-flex justify-content-center mt-5">
        <button class="btn btn-primary" @click="$router.push('/products')">
          Показать еще
        </button>
      </div>
    </section>
    <!-- Signup-->
    <section class="signup-section" id="signup">
      <div class="container px-4 px-lg-5">
        <!-- <div class="row gx-4 gx-lg-5">
                    <div class="col-md-10 col-lg-8 mx-auto text-center">
                        <i class="far fa-paper-plane fa-2x mb-2 text-white"></i>
                        <h2 class="text-white mb-5">Subscribe to receive updates!</h2>

                        <form class="form-signup" id="contactForm" data-sb-form-api-token="API_TOKEN">

                            <div class="row input-group-newsletter">
                                <div class="col"><input class="form-control" id="emailAddress" type="email" placeholder="Enter email address..." aria-label="Enter email address..." data-sb-validations="required,email" /></div>
                                <div class="col-auto"><button class="btn btn-primary disabled" id="submitButton" type="submit">Notify Me!</button></div>
                            </div>
                            <div class="invalid-feedback mt-2" data-sb-feedback="emailAddress:required">An email is required.</div>
                            <div class="invalid-feedback mt-2" data-sb-feedback="emailAddress:email">Email is not valid.</div>

                            <div class="d-none" id="submitSuccessMessage">
                                <div class="text-center mb-3 mt-2 text-white">
                                    <div class="fw-bolder">Form submission successful!</div>
                                    To activate this form, sign up at
                                    <br />
                                    <a href="https://startbootstrap.com/solution/contact-forms">https://startbootstrap.com/solution/contact-forms</a>
                                </div>
                            </div>

                            <div class="d-none" id="submitErrorMessage"><div class="text-center text-danger mb-3 mt-2">Error sending message!</div></div>
                        </form>
                    </div>
                </div> -->
      </div>
    </section>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  data() {
    return {
      product_1: {},
      product_2: {},
    };
  },
  methods: {
    ...mapActions({
      getProducts: "productList/getProducts",
    }),
  },
  computed: {
    ...mapGetters({
      allProducts: "productList/allProducts",
    }),
  },
  async mounted() {
    await this.getProducts();
    this.product_1 = this.allProducts[0];
    this.product_2 = this.allProducts[1];
  },
};
</script>

<style scoped>
.btn-primary {
  color: var(--bs-gray-dark);
  background-color: var(--main-logo-color);
  border-color: var(--main-logo-color);
  padding: 15px 20px;
}

.btn-primary:hover {
  box-shadow: 10px 10px 5px rgb(179, 179, 179) !important;
  transition: 500ms;
}

.image-container {
  height: 30rem;
  position: relative;
}

.image-center {
  width: 100%;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-right: -50%;
  transform: translate(-50%, -50%);
}
</style>