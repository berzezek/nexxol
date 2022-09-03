<template lang="">
  <div class="my-bg">
    <div class="parent-loader" v-if="showLoader">
      <main-loader class="loader-in-center"/>
    </div>
    
    <!-- Section-->
        <section class="py-5" v-else>
            <div class="px-4 px-lg-5 mt-5">
                <div class="row gx-4 gx-lg-5 row-cols-1 row-cols-md-3 row-cols-xl-4 justify-content-center">

                    <product-card 
                      v-for="product in allProducts" 
                      :key="product.id"
                      :id="product.id"
                    />
                  
                </div>
            </div>
            <div class="d-flex justify-content-center mb-3">
              <button class="btn btn-primary" @click="$router.push({name: 'home'})">Вернуться на главную</button>
            </div>
        </section>

        
  </div>
</template>
<script>
import MainLoader from "@/components/special/MainLoader.vue";
import ProductCard from "@/components/product/ProductCard.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  components: {
    ProductCard,
    MainLoader,
  },
  data() {
    return {
      showLoader: true,
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
    this.showLoader = true;

    await this.getProducts();

    this.showLoader = false;

  },
};
</script>
<style scoped>
.btn-primary {
  color: #343a40;
  background-color: #eb5c0e;
  border-color: #eb5c0e;
  padding: 15px 20px;
}

.btn-primary:hover {
  box-shadow: 5px 5px 5px rgb(179, 179, 179) !important;
  transition: 500ms;
}

.parent-loader {
  height: 50em;
  position: relative;
}

.loader-in-center {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-right: -50%;
  transform: translate(-50%, -50%);
}


</style>