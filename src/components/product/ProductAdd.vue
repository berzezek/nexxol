<template>
  <div class="container product-add">
    <form @submit.prevent enctype="multipart/form-data">
      <div class="mb-3">
        <label class="form-label">Категория</label>
        <select
          class="form-select"
          aria-label="Default select example"
          v-model="product.category"
        >
          <option selected disabled>Категория</option>
          <option
            v-for="category in allCategories"
            :key="category.id"
            :value="category.id"
          >
            {{ category.name }}
          </option>
        </select>
        <div class="form-text">Выберите или добавьте новую</div>
      </div>

      <div class="mb-3">
        <label for="exampleInputName" class="form-label"
          >Название продукта</label
        >
        <input
          type="text"
          class="form-control"
          id="exampleInputName"
          aria-describedby="nameHelp"
          v-model="product.name"
        />
        <div class="form-text">Обязательное поле</div>
      </div>

      <div class="mb-3">
        <label for="description" class="form-label">Описание продукта</label>
        <input
          type="text"
          class="form-control"
          id="description"
          aria-describedby="descriptionHelp"
          v-model="product.description"
        />
        <div class="form-text">По желанию</div>
      </div>

      <div class="mb-3">
        <label for="image1" class="form-label">Главное изображение</label>
        <input
          class="form-control"
          type="file"
          id="image1"
          @input="image1Upload"
        />
      </div>
      <div class="mb-3">
        <label for="image2" class="form-label"
          >Дополнительное изображение</label
        >
        <input class="form-control" type="file" id="image2" />
      </div>
      <div class="mb-3">
        <label for="image3" class="form-label"
          >Дополнительное изображение</label
        >
        <input class="form-control" type="file" id="image3" />
      </div>

      <div class="mb-3">
        <label for="price" class="form-label">Цена за единицу</label>
        <input
          type="numer"
          class="form-control"
          id="price"
          aria-describedby="price"
          v-model="product.price"
        />
        <div class="form-text">Цена в UZS</div>
      </div>

      <div class="mb-3">
        <label for="discount" class="form-label">Скидка</label>
        <input
          type="numer"
          class="form-control"
          id="discount"
          aria-describedby="discountHelp"
          v-model="product.discount"
        />
        <div class="form-text">Округляется до 900</div>
      </div>

      <div class="mb-3">
        <label class="form-label">Единица измерения</label>
        <select
          class="form-select"
          aria-label="Default select example"
          v-model="product.unit"
        >
          <option selected>Open this select menu</option>
          <option value="L">Л.</option>
          <option value="Pcs">Шт.</option>
        </select>
        <div class="form-text">Единица измерения</div>
      </div>

      <div class="mb-3">
        <label for="sku" class="form-label">Артикул</label>
        <input
          type="text"
          class="form-control"
          id="sku"
          aria-describedby="skuHelp"
          v-model="product.sku"
        />
        <div class="form-text">Необязательное поле</div>
      </div>

      <div class="mb-3 form-check">
        <input
          type="checkbox"
          class="form-check-input"
          id="isActive"
          v-model="product.isActive"
        />
        <label class="form-check-label" for="showInCatalog"
          >Показать на сайте</label
        >
      </div>

      <button class="btn btn-primary me-3" @click="addProduct">Добавить</button>

      <button class="btn btn-primary" @click="$router.go(-1)">Назад</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import axios from "axios";
export default {
  data() {
    return {
      product: {
        category: "",
        name: "",
        description: "",
        discount: "",
        unit: "",
        price: "",
        sku: "",
        isActive: true,
      },
      selectImage1: null,
      selectImage2: null,
      selectImage3: null,
    };
  },
  methods: {
    ...mapActions({
      getCategories: "categoryList/getCategories",
    }),
    image1Upload(e) {
      this.selectImage1 = e.target.files[0];
    },
    async addProduct() {
      let fd = new FormData();

      if (this.selectImage1) {
        fd.append("image_1", this.selectImage1, this.selectImage1.name);
        console.log(fd);
      }

      fd.append("category", this.product.category);
      fd.append("name", this.product.name);
      fd.append("description", this.product.description);
      fd.append("discount", this.product.discount);
      fd.append("unit", this.product.unit);
      fd.append("price", this.product.price);
      fd.append("sku", this.product.sku);
      fd.append("isActive", this.product.isActive);
      await axios.post(`product/`, fd, {
        headers: {
          Authorization: `Token ${window.localStorage.token}`,
        },
      });
    },
  },
  computed: {
    ...mapGetters({
      allCategories: "categoryList/allCategories",
    }),
  },
  mounted() {
    this.getCategories();
  },
};
</script>

<style scoped>
.product-add {
  margin-top: 8rem;
  margin-bottom: 2rem;
}
</style>