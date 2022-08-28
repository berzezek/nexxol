<template lang="">
  <div>
    <!-- Section-->
        <section class="py-5">
            <div class="container px-4 px-lg-5 mt-5">
                <div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center">
                  <product-card></product-card>
                </div>
            </div>
        </section>
  </div>
</template>
<script>
import ProductCard from '@/components/product/ProductCard.vue';
import {mapActions, mapGetters} from 'vuex'
export default {
  components: {
    ProductCard
  },
  methods: {
    ...mapActions({
      getProducts: 'productList/getProducts'
    })
  },
  computed: {
    ...mapGetters({
      allProducts: 'productList/allProducts'
    })
  },
  async mounted() {
    await this.getProducts()
  }
}
</script>
<style lang="">
  
</style>