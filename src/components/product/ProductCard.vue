<template lang="">
<div class="col mb-5">

  
  <div class="card h-100" @click="$router.push({name: 'product-detail', params: {id: $props.id}})">
      <!-- Sale badge-->
      <div class="badge bg-dark text-white position-absolute" style="top: 0.5rem; right: 0.5rem; z-index: 1" v-if="product.discount > 0">Sale</div>
      <!-- Product image-->
        <div class="image-container">
          <div v-if="product.image_1" class="image-center">
            <img :src="product.image_1" class="card-img-top" :alt="product.name"/>
          </div>

          
          <div v-else class="image-center"> 
            <img :src="product.get_thumbnail" class="card-img-top" :alt="product.name"/>
          </div>
        </div>
          
      <!-- <img class="card-img-top" :src="product.get_thumbnail" :alt="product.name" /> -->
      <!-- Product details-->
      <div class="card-body p-4" v-cloak>
          <div class="text-center">
              <!-- Product name-->
              <h5 class="fw-bolder">{{ product.name }}</h5>
              <!-- Product reviews-->
              <!-- <div class="d-flex justify-content-center small text-warning mb-2">
                  <div class="bi-star-fill"></div>
                  <div class="bi-star-fill"></div>
                  <div class="bi-star-fill"></div>
                  <div class="bi-star-fill"></div>
                  <div class="bi-star-fill"></div>
              </div> -->
              <!-- Product price-->
              <div v-if="product.discount > 0">
                <span class="text-muted text-decoration-line-through">{{ beautyPrice }} </span>
              {{ beautyDiscount }} UZS
              </div>
              <div v-else >
              {{ beautyPrice }} UZS
              </div>
              
          </div>
      </div>
      <!-- Product actions-->
      <!-- <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
          <div class="text-center"><a class="btn btn-outline-dark mt-auto" @click="$router.push({name: 'product-detail', params: {id: $props.id}})">Подробнее</a></div>
      </div> -->
  </div>
</div>

</template>
<script>
import { mapActions, mapGetters } from "vuex";
export default {
  data() {
    return {
      product: {},
    };
  },
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  methods: {
    ...mapActions({
      getProduct: "productDetail/getProduct",
    }),
  },
  computed: {
    ...mapGetters({
      myProduct: "productDetail/myProduct",
    }),
    beautyPrice() {
      return Math.floor(this.product.price)
        .toString()
        .replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    },
    beautyDiscount() {
      return Math.floor(this.product.discount_price)
        .toString()
        .replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    },
  },
  async mounted() {
    await this.getProduct(this.$props.id);
    this.product = this.myProduct;
  },
};
</script>
<style scoped>
.card {
  opacity: 0.9;
}

.card:hover {
  box-shadow: 5px 5px 5px rgb(179, 179, 179);
  transition: 500ms;
  opacity: 1;
}

.image-container {
  height: 20rem;
  position: relative;
}

.image-center {
  height: 100%;
  width: 100%;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-right: -50%;
  transform: translate(-50%, -50%);
}
</style>