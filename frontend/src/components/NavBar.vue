<script setup>
import { ref } from 'vue';
import TestView from './views/TestView.vue';
import HomeView from './views/HomeView.vue'
import {useRoute, useRouter} from 'vue-router'
import Menubar from 'primevue/menubar';


const router = useRouter()
const route = useRoute()
const items = ref([
    {
        label: 'Home',
        icon: 'pi pi-home',
        route: '/'
    },
    // {
    //     label: 'Projects',
    //     icon: 'pi pi-clipboard',
    // },
    {
        label: 'Test',
        icon: 'pi pi-book',
        route: '/test'
    }
]);

// const routes = [
//   {path: '/', component: HomeView},
//   {path: '/questionnaire', component: TestView}
// ]

</script>

<template>
  <Menubar :model="items">
    <template #item="{ item, props}">
      <router-link v-slot="{ href, navigate }" :to="item.route" custom>
        <a :href="href" v-bind="props.action" @click="navigate">
          <span :class="item.icon" />
          <span>{{ item.label }}</span>
        </a>
      </router-link>
    </template>
  </Menubar>

<!--   <nav>-->
<!--      <RouterLink to="/">Home</RouterLink>-->
<!--      <RouterLink to="/test">Test</RouterLink>-->
<!--   </nav>-->


</template>