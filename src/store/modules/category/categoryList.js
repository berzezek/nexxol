import axios from "axios";
export default {
  state: () => ({
    categories: [],
  }),
  actions: {
    async getCategories(ctx) {
      await axios.get(`category/`).then(response => {
        const categories = response.data
        ctx.commit('updateCategories', categories);
      });
      
    }
  },
  mutations: {
    updateCategories(state, categories) {
      state.categories = categories;
    }
  },
  getters: {
    allCategories(state) {
      return state.categories
    }
  },
  namespaced: true
}