<template>
  <div class="container dashboard">
    <h3 class="text-center my-5">Панель управления</h3>

    <table class="table table-striped table-hover">
      <thead>
        <tr>
          <th scope="col">Наименование</th>
          <th scope="col">Изображение</th>
          <th scope="col">Активно</th>
          <th scope="col">Цена</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="product in allProducts"
          :key="product.id"
          @click="$router.push({ name: 'product-edit', params: { id: product.id } })"
          
        >
          <td>
            {{ product.name }}
          </td>
          <td>
            <img
              :src="product.get_thumbnail"
              :alt="product.name"
              class="img-fluid table-img"
            />
          </td>
          <td>
            <i class="fa-solid fa-check" v-if="product.isActive"></i>
            <i class="fa-solid fa-xmark" v-else></i>
          </td>
          <td>
            {{ product.price }}
          </td>
        </tr>
      </tbody>
    </table>
    <button class="btn btn-success me-3" @click="$router.push({name: 'product-add'})">
      Добавить продукт
    </button>
    <button class="btn btn-info" @click="$router.push('/products')">
      Вернуться к продуктам
    </button>

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
      getProducts: "productList/getProducts",
    }),
  },
  computed: {
    ...mapGetters({
      allProducts: "productList/allProducts",
    }),
  },
  mounted() {
    this.getProducts();
  },
};
</script>

<style scoped>
.table-img {
  width: 50px;
}
</style>