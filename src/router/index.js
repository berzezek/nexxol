import { createRouter, createWebHistory } from "vue-router";


const router = createRouter({
  history: createWebHistory(),
  routes: [
    {path: '/', name: 'home', component: () => import('@/views/MainPage.vue')},
    {path: '/products', name: 'products', component: () => import('@/components/product/ProductList.vue')},
    {path: '/product-detail/:id', name: 'product-detail', component: () => import('@/components/product/ProductDetail.vue'), props: true},
    {path: '/dashboard', name: 'dashboard', component: () => import('@/components/dashboard/DashBoard.vue')},
    {path: '/category-add', name: 'category-add', component: () => import('@/components/category/CategoryAdd.vue')},
    {path: '/product-add', name: 'product-add', component: () => import('@/components/product/ProductAdd.vue')}
  ] 
})

export default router;