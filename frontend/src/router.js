import { createWebHistory, createRouter } from 'vue-router'

import HomeView from './components/views/HomeView.vue'
import TestView from './components/views/TestView.vue'
import TestResultView from './components/views/TestResultView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/test', component: TestView},
  { path: '/results', component: TestResultView}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router