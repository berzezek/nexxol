<template lang="">
<div class="dashboard my-5">
  <br/>
  <br/>

      <div class="container col-md-4 card">
        <div class="img-detail">
          <div class="badge bg-dark text-white position-absolute" style="top: 1rem; right: 1rem" v-if="myProduct.discount > 0"> Sale </div>
          
          <div v-if="myProduct.image_1">
            <img :src="myProduct.image_1" class="image-thumbnail card-image" />
          </div>

          
          <div v-else>
            <img :src="myProduct.get_thumbnail" class="image-thumbnail card-image" />
          </div>
          
          <h3 class="ms-3 mt-2">
            <b>{{ myProduct.name }}</b>
          </h3>
          
        </div>
        <div class="container col-md-10 col-lg-8 mb-4 text-center">
          <p class="text-start">{{ myProduct.description }}</p>
          <div v-if="myProduct.discount > 0" >
              <h5 class="text-muted text-decoration-line-through">{{ beautyPrice }} </h5>
              <h5 class="display-6">{{ beautyDiscount }} UZS</h5>
          </div>
          <div v-else>
          <h5 class="display-6">{{ beautyPrice }} UZS</h5>
          </div>
        </div>
      </div>
      <div class="d-flex justify-content-center my-3">
        <button class="btn btn-success" @click="$router.go(-1)">Вернуться</button>
      </div>
      <br/>
  <br/>
  <br/>
  <br/>
    </div>
</template>
<script>
import { mapActions, mapGetters } from "vuex";
export default {
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
      return Math.floor(this.myProduct.price)
        .toString()
        .replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    },
    beautyDiscount() {
      return Math.floor(this.myProduct.discount_price)
        .toString()
        .replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    },
  },
  mounted() {
    this.getProduct(this.$attrs.id);
  },
};
</script>
<style scoped>
.card-image {
  width: 100%;
}
</style>