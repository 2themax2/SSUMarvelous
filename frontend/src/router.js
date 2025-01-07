import { createWebHistory, createRouter } from 'vue-router'

import HomeView from './components/views/homeView.vue'
import TestView from './components/views/TestView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/test', component: TestView},
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router