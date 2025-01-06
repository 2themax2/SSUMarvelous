<template>
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
<script setup>
import Button from 'primevue/button'
import { Form } from '@primevue/forms'
import QuestionBox from './QuestionBox.vue'
import { useToast } from "primevue/usetoast";
import {Toast} from "primevue";

import {inject, ref} from "vue";
const questions = inject('questions')
const toast = useToast();

// Create a reactive array to keep track of answers (e.g., scores)
const answers = ref(Array(questions.length).fill(null));

// Handle response count updates
const handleResponse = (index, count) => {
  answers.value[index] = count.value;
};

// Form submit handler
const handleSubmit = () => {
    toast.add({ severity: 'success', summary: 'Form is submitted.' })
    console.log('answers:', answers.value);
};
</script>