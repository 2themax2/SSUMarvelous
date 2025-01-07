<script setup>
import Button from 'primevue/button'
import { Form } from '@primevue/forms'
import QuestionBox from '../QuestionBox.vue'
import { useToast } from "primevue/usetoast";
import {Toast} from "primevue";
import {onMounted, ref} from "vue";
import axios from "axios";
import { useRoute, useRouter } from 'vue-router'

const router = useRouter()
const route = useRoute()

const questions = ref([])
onMounted(()=> {
  axios.get('http://127.0.0.1:8000/RoleTest/').then((response) => {
    console.log(response.data)
    questions.value = response.data
  })
});

const toast = useToast();

// Create a reactive array to keep track of answers (e.g., scores)
const answers = ref(Array(questions.length).fill(null));

// Handle response count updates
const handleResponse = (index, count) => {
  answers.value[index] = count.value;
};

const token = ref()
// Form submit handler
const handleSubmit = () => {
  console.log('answers:', answers.value);
  axios.get('http://127.0.0.1:8000/csrf-token/').then((response) => {
    console.log(response.data)
    token.value = response.data.csrfToken
    axios.post('http://127.0.0.1:8000/Student/calculate_scores/', {answers: answers.value}, {
      headers: {'Content-Type': 'application/json',
        'X-CSRFToken': token.value
      },
      credentials: 'include', // Stuurt cookies naar de backend
    })
        .then(response => {
          console.log('Response', response.data)
          toast.add({ severity: 'success', summary: 'Form is submitted.' })
          router.push('/results')
        })
        .catch(err => {console.log(err)} )
     })
      .catch(err => {console.log(err)} )
};

</script>
<template>
  <header class="header-section">
      <h1 class="text-left">Test</h1>
  </header>
  <div class="card flex justify-center">
    <Toast />
    <Form v-slot="$form" @submit="handleSubmit"  >
    <div v-for="(question, index) in questions" :key="index" class="flex  gap-2">
      <p>
      Question {{index + 1}}:
      </p>
      <QuestionBox
          :question="question"
          @answered="handleResponse(index, $event)"
        />
    </div>
    <Button type="submit" severity="success" label="Submit" />

  </Form>
  </div>
</template>