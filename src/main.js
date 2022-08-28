import { createApp } from 'vue'
import router from '@/router/'
import store from '@/store/'
import axios from 'axios'
import '@/css/styles.css'
import '@/css/product.css'
import App from './App.vue'

axios.defaults.baseURL = 'http://localhost:8000/api/v1/';

createApp(App)
  .use(router)
  .use(store)
  .mount('#app')
