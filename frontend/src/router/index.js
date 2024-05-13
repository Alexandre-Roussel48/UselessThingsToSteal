import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/inventory',
      name: 'inventory',
      component: () => import('../views/InventoryView.vue')
    },
    {
      path: '/vault',
      name: 'vault',
      component: () => import('../views/VaultView.vue')
    },
    {
      path: '/forge',
      name: 'forge',
      component: () => import('../views/ForgeView.vue')
    },
    {
      path: '/theft',
      name: 'theft',
      component: () => import('../views/TheftView.vue')
    },
    {
      path: '/drop',
      name: 'drop',
      component: () => import('../views/DropView.vue')
    },
    {
      path: '/me',
      name: 'me',
      component: () => import('../views/MeView.vue')
    },
  ]
})

export default router