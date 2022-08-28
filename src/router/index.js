import { createRouter, createWebHistory } from "vue-router";


const router = createRouter({
  history: createWebHistory(),
  routes: [
    {path: '/', name: 'home', component: () => import('@/views/MainPage.vue')},
    {path: '/products', name: 'products', component: () => import('@/components/product/ProductList.vue')},
    {path: '/dashboard', name: 'dashboard', component: () => import('@/components/dashboard/DashBoard.vue')},
    {path: '/product-add', name: 'product-add', component: () => import('@/components/product/ProductAdd.vue')}
  ] 
})

export default router;