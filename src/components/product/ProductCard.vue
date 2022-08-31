<template lang="">
<div class="col mb-5">

  
  <div class="card h-100" @click="$router.push({name: 'product-detail', params: {id: $props.id}})">
      <!-- Sale badge-->
      <div class="badge bg-dark text-white position-absolute" style="top: 0.5rem; right: 0.5rem" v-if="product.discount > 0">Sale</div>
      <!-- Product image-->
          <div v-if="product.image_1">
            <img :src="product.image_1" class="card-img-top" />
          </div>

          
          <div v-else>
            <img :src="product.get_thumbnail" class="card-img-top" />
          </div>
      <!-- <img class="card-img-top" :src="product.get_thumbnail" :alt="product.name" /> -->
      <!-- Product details-->
      <div class="card-body p-4">
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
import axios from "axios";
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
    async getProduct(id) {
      await axios.get(`product/${id}/`).then((response) => {
        this.product = response.data;
      });
    },
  },
  computed: {
    // ...mapGetters({
    //   myProduct: 'productDetail/myProduct'
    // }),
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
  mounted() {
    this.getProduct(this.$props.id);
  },
};
</script>
<style scoped>
.card {
  box-shadow: 10px 10px 5px rgb(179, 179, 179);
}
.card:hover {
  box-shadow: none;
  transition: 500ms;
}
</style>