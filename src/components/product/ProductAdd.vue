<template>
  <div class="container product-add">
    <form @submit.prevent enctype="multipart/form-data">
      <div class="mb-3">
        <label class="form-label">Category</label>
        <select
          class="form-select"
          aria-label="Default select example"
          v-model="product.category"
        >
          <option selected>Open this select menu</option>
          <option
            v-for="category in allCategories"
            :key="category.id"
            :value="category.id"
          >
            {{ category.name }}
          </option>
        </select>
        <div class="form-text">Input product category</div>
      </div>

      <div class="mb-3">
        <label for="exampleInputName" class="form-label">Product name</label>
        <input
          type="text"
          class="form-control"
          id="exampleInputName"
          aria-describedby="nameHelp"
          v-model="product.name"
        />
        <div class="form-text">Input product name</div>
      </div>

      <div class="mb-3">
        <label for="description" class="form-label">Product description</label>
        <input
          type="text"
          class="form-control"
          id="description"
          aria-describedby="descriptionHelp"
          v-model="product.description"
        />
        <div class="form-text">Input product description</div>
      </div>

      <div class="mb-3">
        <label for="image1" class="form-label">Image</label>
        <input
          class="form-control"
          type="file"
          id="image1"
          @change="image1Upload"
        />
      </div>
      <div class="mb-3">
        <label for="image2" class="form-label">Image</label>
        <input class="form-control" type="file" id="image2" />
      </div>
      <div class="mb-3">
        <label for="image3" class="form-label">Image</label>
        <input class="form-control" type="file" id="image3" />
      </div>

      <div class="mb-3">
        <label for="price" class="form-label">Price</label>
        <input
          type="numer"
          class="form-control"
          id="price"
          aria-describedby="price"
          v-model="product.price"
        />
        <div class="form-text">price in UZS</div>
      </div>

      <div class="mb-3">
        <label for="discount" class="form-label">Discount</label>
        <input
          type="numer"
          class="form-control"
          id="discount"
          aria-describedby="discountHelp"
          v-model="product.discount"
        />
        <div class="form-text">Aufrundung auf 9000</div>
      </div>

      <div class="mb-3">
        <label class="form-label">Unit</label>
        <select
          class="form-select"
          aria-label="Default select example"
          v-model="product.unit"
        >
          <option selected>Open this select menu</option>
          <option value="L">L</option>
          <option value="Pcs">Pcs</option>
        </select>
        <div class="form-text">Input product category</div>
      </div>

      <div class="mb-3">
        <label for="sku" class="form-label">Product sku</label>
        <input
          type="text"
          class="form-control"
          id="sku"
          aria-describedby="skuHelp"
          v-model="product.sku"
        />
        <div class="form-text">Input product sku</div>
      </div>

      <div class="mb-3 form-check">
        <input
          type="checkbox"
          class="form-check-input"
          id="isActive"
          v-model="product.isActive"
        />
        <label class="form-check-label" for="showInCatalog">Is Active</label>
        <div id="showInCatalog" class="form-text">Show in catalog</div>
      </div>

      <button type="submit" class="btn btn-primary" @click="addProduct">
        Submit
      </button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import axios from 'axios';
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
      selectImgage1: null,
      selectImgage2: null,
      selectImgage3: null,
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

      if (this.selectImgage1) {
        fd.append("image1", this.selectImage1, this.selectImage1.name);
      }
      
      fd.append("category", this.product.category);
      fd.append("name", this.product.name);
      fd.append("description", this.product.description);
      fd.append("discount", this.product.discount);
      fd.append("unit", this.product.unit);
      fd.append("price", this.product.price);
      fd.append("sku", this.product.sku);
      fd.append("isActive", this.product.isActive);
      await axios.post(`/category/${this.product.category}/product/`, this.product)
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