import axios from "axios";
export default {
  state: () => ({
    products: [],
  }),
  actions: {
    async getProducts(ctx) {
      await axios.get(`category/product/`).then(response => {
        const products = response.data
        ctx.commit('updateProducts', products);
      });
      
    }
  },
  mutations: {
    updateProducts(state, products) {
      state.products = products;
    }
  },
  getters: {
    allProducts(state) {
      return state.products
    }
  },
  namespaced: true
}