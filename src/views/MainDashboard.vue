<template>
  <div class="table-responsive">
    <button class="btn">Add new product</button>
    <table class="table tablesorter" id="">
      <thead class="text-primary">
        <tr>
          <th>Name</th>
          <th>Image</th>
          <th>Active</th>
          <th class="text-center">Price</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in allProduct" :key="product.id">
          <td>
            {{ product.name }}
          </td>
          <td>
            <img :srd="product.image1" :alt="product.name" />
          </td>
          <td>
            {{ product.isActive }}
          </td>
          <td class="text-center">
            {{ product.price }}
          </td>
        </tr>
      </tbody>
    </table>
    <button class="btn">Add new product</button>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  props: {
    user: {
      type: String,
    },
  },
  methods: {
    ...mapActions({
      productGet: "productList/productGet",
    }),
  },
  computed: {
    ...mapGetters({
      allProduct: "productList/allProduct",
    }),
  },
  mounted() {
    this.productGet();
  },
};
</script>

<style scoped>
@import "@/css/nucleo-icons.css";
@import "@/css/black-dashboard.css";
</style>