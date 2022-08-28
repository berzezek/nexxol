import { createStore } from 'vuex';
import loginPost from '@/store/modules/login/loginPost';
import loginGet from '@/store/modules/login/loginGet';
import productList from '@/store/modules/product/productList';
import categoryList from '@/store/modules/category/categoryList';

const store = createStore({
  modules: {
    loginPost,
    productList,
    categoryList,
    loginGet
  }
})

export default store;