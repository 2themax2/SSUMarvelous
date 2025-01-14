import { createWebHistory, createRouter } from 'vue-router'

import HomeView from './components/views/HomeView.vue'
import TestView from './components/views/TestView.vue'
import TestResultView from './components/views/TestResultView.vue'
import ProjectsView from "./components/views/ProjectsView.vue";
import ProjectDetailView from "./components/views/ProjectDetailView.vue";

const routes = [
  { path: '/', component: HomeView },
  { path: '/test', component: TestView},
  { path: '/results', component: TestResultView},
  { path: '/projects', component: ProjectsView},
  { path: '/projects/:id', component: ProjectDetailView, props:true}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router