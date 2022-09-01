<template lang="">
<div class="dashboard my-bg">
  <br/>
  <br/>
  <br/>
  <br/>

      <div class="container col-md-4 card">
        <div class="img-detail">
          <div class="btn btn-dark text-white position-absolute text-muted" style="top: 2rem; right: 2rem" v-if="myProduct.discount > 0"> Sale </div>
          
          <div v-if="myProduct.image_1">
            <img :src="myProduct.image_1" class="image-thumbnail card-image" />
          </div>

          
          <div v-else>
            <img :src="myProduct.get_thumbnail" class="image-thumbnail card-image" />
          </div>
          
          <h3 class="ms-3 my-2">
            <b>{{ myProduct.name }}</b>
          </h3>
          
        </div>
        <div class="ms-3">
          <p class="text-start text-muted">{{ myProduct.description }}</p>
          <div v-if="myProduct.discount > 0" class="text-end">
              <span class="text-muted text-decoration-line-through">{{ beautyPrice }}</span>
              <h4>{{ beautyDiscount }}</h4>
          </div>
          <div v-else>
          <h5 class="display-6">{{ beautyPrice }}</h5>
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