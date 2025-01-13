import { createWebHistory, createRouter } from 'vue-router'

import HomeView from './frontend/src/components/views/HomeView.vue'
import TestView from './frontend/src/components/views/TestView.vue'
import TestResultView from './frontend/src/components/views/TestResultView.vue'

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