import "./assets/main.css"
import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import Lara from '@primevue/themes/lara';
import 'primeflex/primeflex.css'
import ToastService from 'primevue/toastservice';
import 'primeicons/primeicons.css'
import router from './router'

const app = createApp(App)
app.use(PrimeVue, {
  theme: {
    preset: Lara,
    options: {
      prefix: 'p',
      darkModeSelector: 'none',
      cssLayer: false
    }
  }});
app.use(router)
app.use(ToastService)
app.mount('#app')



