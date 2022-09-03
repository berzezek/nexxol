import { createApp } from 'vue'
import router from '@/router/'
import store from '@/store/'
import axios from 'axios'
import Toaster from "@meforma/vue-toaster";

import '@/css/styles.css'
import '@/css/product.css'
import App from './App.vue'

axios.defaults.baseURL = 'http://localhost:8000/api/v1/';
// axios.defaults.baseURL = 'http://nixxol.uz/api/v1/';

createApp(App)
  .use(router)
  .use(store)
  .use(Toaster, {
    // One of the options
    position: "top",
    duration: 3000
  })
  .mount('#app')
