<template lang="">
  <div class="container my-5">
    <br/>
    <br/>
    <br/>
    <br/>
  <form @submit.prevent>
    <div class="mb-3">
      <label for="category" class="form-label">Наименование категории</label>
      <input type="text" class="form-control" id="category" v-model="category">
    </div>

    <button type="submit" class="btn btn-primary me-3" @click="addCategory">Добавить</button>
    <button type="submit" class="btn btn-primary" @click="$router.go(-1)">Назад</button>
  </form>
    <br/>
    <br/>
    <br/>
    <br/>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      category: "",
    };
  },
  methods: {
    async addCategory() {
      if (this.category !== "") {
        await axios
          .post(
            "category/",
            { name: this.category },
            {
              headers: {
                Authorization: `Token ${window.localStorage.token}`,
              },
            }
          )
          .then((res) => {
            if (res.status === 201) {
              this.$toast.success(`Категория: ${res.data.name} - успешно добавлена!`);
              this.category = "";
            } else {
              this.$toast.error("Произошла ошибка :(");
            }
          });
      } else {
        this.$toast.info("Заполните название категории!");
      }
    },

  },
};
</script>
<style lang="">
</style>