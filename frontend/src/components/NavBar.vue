<script setup>
import { ref } from 'vue';
import TestView from './views/TestView.vue';
import HomeView from './views/HomeView.vue'
import {useRoute, useRouter} from 'vue-router'

const router = useRouter()
const route = useRoute()
// const items = ref([
//     {
//         label: 'Home',
//         icon: 'pi pi-home',
//         route: '/'
//     },
//     {
//         label: 'Projects',
//         icon: 'pi pi-clipboard',
//     },
//     {
//         label: 'Questionnaire',
//         icon: 'pi pi-book',
//         route: '/questionnaire'
//     }
// ]);

const routes = [
  {path: '/', component: HomeView},
  {path: '/questionnaire', component: TestView}
]

</script>

<template>
<!--  <Menubar :model="items">-->
<!--    <template #item="{ item, props, hasSubmenu }">-->
<!--      <RouterLink to="item.route" custom>-->
<!--        <span :class="item.icon" />-->
<!--        <span>{{ item.label }}</span>-->
<!--      </RouterLink>-->
<!--&lt;!&ndash;          <RouterLink>&ndash;&gt;-->
<!--&lt;!&ndash;            <span :class="item.icon" />&ndash;&gt;-->
<!--&lt;!&ndash;            <span>{{ item.label }}</span>&ndash;&gt;-->
<!--&lt;!&ndash;          </RouterLink>&ndash;&gt;-->
<!--    </template>-->
<!--  </Menubar>-->

  <RouterLink to="/">Home</RouterLink>
  <RouterLink to="/questionnaire">Test</RouterLink>


</template>