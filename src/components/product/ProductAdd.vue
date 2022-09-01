<template>
  <div class="container product-add">
    <h3 class="text-center mt-5">Добавить продукт</h3>
    <form @submit.prevent enctype="multipart/form-data" class="border rounded p-5 my-3">
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
        <div class="form-text">Выберите или добавьте <span @click="$router.push({name: 'category-add'})" class="text-primary">новую</span></div>
      </div>

      <div class="mb-3">
        <label for="exampleInputName" class="form-label"
          >Название продукта</label
        >
        <input
          type="text"
          maxlength=255
          class="form-control"
          id="exampleInputName"
          aria-describedby="nameHelp"
          v-model="product.name"
        />
        <div class="form-text">Название должно быть уникальным, максимальная длинна 64 символа</div>
      </div>

      <div class="mb-3">
        <label for="description" class="form-label">Описание продукта</label>
        <textarea
          type="text"
          class="form-control"
          id="description"
          aria-describedby="descriptionHelp"
          v-model="product.description" />
          <div class="form-text">Введите описание продукта</div>
      </div>

      <div class="mb-3">
        <label for="image1" class="form-label">Главное изображение</label>
        <input
          class="form-control"
          type="file"
          accept="image/png, image/jpeg"
          id="image1"
          @input="image1Upload"
        />
      </div>
      <div class="mb-3">
        <label for="image2" class="form-label"
          >Дополнительное изображение</label
        >
        <input class="form-control" type="file" accept="image/png, image/jpeg" id="image2" />
      </div>
      <div class="mb-3">
        <label for="image3" class="form-label"
          >Дополнительное изображение</label
        >
        <input class="form-control" type="file" accept="image/png, image/jpeg"  id="image3" />
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
        <div class="form-text">Цена - Цена * скидку - 100 (~ X XXX 900)</div>
      </div>

      <div class="mb-3">
        <label class="form-label">Объём</label>
        <input
          type="text"
          class="form-control"
          id="unit"
          aria-describedby="unitHelp"
          v-model="product.unit"
        />
        <div class="form-text">Объем упаковки</div>
      </div>

      <div class="mb-3">
        <label for="product_mark" class="form-label">Артикул</label>
        <input
          type="text"
          class="form-control"
          id="product_mark"
          aria-describedby="product_markHelp"
          v-model="product.product_mark"
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
        product_mark: "",
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
      }

      if (this.selectImage2) {
        fd.append("image_2", this.selectImage2, this.selectImage2.name);
      }

      if (this.selectImage3) {
        fd.append("image_3", this.selectImage3, this.selectImage3.name);
      }

      fd.append("category", this.product.category);
      fd.append("name", this.product.name);
      fd.append("description", this.product.description);
      fd.append("discount", this.product.discount);
      fd.append("unit", this.product.unit);
      fd.append("price", this.product.price);
      fd.append("product_mark", this.product.product_mark);
      fd.append("isActive", this.product.isActive);
      await axios.post(`product/`, fd, {
        headers: {
          Authorization: `Token ${window.localStorage.token}`,
        },
      })
      .then(res => {
        if (res.status === 201) {
          this.$toast.success('Продукт добавлен')
        } else {
         this.$toast.info( 'Проверьте правильность заполнения полей')
        }
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