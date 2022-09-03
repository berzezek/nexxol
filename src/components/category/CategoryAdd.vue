<template lang="">
  <div class="container">
  <h3 class="text-center mt-5">Добавить категорию</h3>
  <form @submit.prevent class="border rounded p-5 my-3">
    
    <div class="mb-3">
      <label for="category" class="form-label">Наименование категории</label>
      <input type="text" class="form-control" id="category" v-model="category">
    </div>

    <button type="submit" class="btn btn-primary me-3" @click="addCategory">Добавить</button>
    <button type="submit" class="btn btn-primary" @click="$router.go(-1)">Назад</button>
  </form>
  <div class="container col-md-8 mt-5">
    <h3 class="text-center">Существующие категории</h3>
    <table class="table table-striped table-hover">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Наименование</th>
          <th scope="col">Опции *</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="category, index in allCategories" :key="category.id" >
          <th scope="row">{{ index + 1 }}</th>
          <td :class="{'text-muted text-decoration-line-through': !category.isActive}">{{ category.name }}</td>
          <td v-if="category.isActive" @click="categoryDelete(category.id, category.name)" class="text-danger text-center">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-x" viewBox="0 0 16 16">
              <path d="M6.146 6.146a.5.5 0 0 1 .708 0L8 7.293l1.146-1.147a.5.5 0 1 1 .708.708L8.707 8l1.147 1.146a.5.5 0 0 1-.708.708L8 8.707 6.854 9.854a.5.5 0 0 1-.708-.708L7.293 8 6.146 6.854a.5.5 0 0 1 0-.708z"/>
              <path d="M4 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H4zm0 1h8a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1z"/>
            </svg>
          </td>
          <td v-else @click="categoryUnDelete(category.id, category.name)" class="text-success text-center">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bookmark-check" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M10.854 5.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7.5 7.793l2.646-2.647a.5.5 0 0 1 .708 0z"/>
              <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/>
            </svg>
          </td>
        </tr>
      </tbody>
    </table>
    <p class="text-muted">* Удаление категории повлечет скрытие с сайта всех связанных с ней продуктов </p>
  </div>

  </div>
</template>
<script>
import axios from "axios";
import { mapActions, mapGetters } from "vuex";
export default {
  data() {
    return {
      category: "",
    };
  },
  methods: {
    ...mapActions({
      getCategories: "categoryList/getCategories",
    }),
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
              this.$toast.success(
                `Категория: ${res.data.name} - успешно добавлена!`
              );
              this.category = "";
              // this.$router.go(-1);
            } else {
              this.$toast.error("Произошла ошибка :(");
            }
          });
      } else {
        this.$toast.info("Заполните название категории!");
      }
    },
    categoryDelete(id, name) {
      axios.put(
        `category/${id}/`, {isActive: false, name: name}, 
        {
          headers: {
            Authorization: `Token ${window.localStorage.token}`,
          },
        }
      )
      .then(res => {
        if (res.status === 200) {
          this.$toast.info(
            `Категория "${name}" не активна!`
          );
        } else {
          this.$toast.error('Произошла ошибка')
        }
      })
    },
    categoryUnDelete(id, name) {
      axios.put(
        `category/${id}/`, {isActive: true, name: name}, 
        {
          headers: {
            Authorization: `Token ${window.localStorage.token}`,
          },
        }
      )
      .then(res => {
        if (res.status === 200) {
          this.$toast.info(
            `Категория "${name}" активна!`
          );
        } else {
          this.$toast.error('Произошла ошибка')
        }
      })
    },
  },
  computed: {
    ...mapGetters({
      allCategories: "categoryList/allCategories",
    }),
  },
  watch: {
    allCategories(newval) {
      if (newval) {
        this.getCategories()
      }
    }
  },
  async mounted() {
    await this.getCategories();
  },
};
</script>
<style lang="">
</style>