<template>
<!--  {{questions}}-->
  <form @submit.prevent="handleSubmit">
    <div v-for="(question, index) in questions" :key="index">
      <p>
      Question {{index + 1}}: {{question.question}}
      </p>
      <QuestionBox
          :question="question"
          @answered="handleResponse(index, $event)"
        />
      <p>Antwoord: {{ answers[index] || 'Nog geen antwoord' }}</p>
    </div>
    <button type="submit">Verzenden</button>
  </form>

</template>
<script setup>
// import Button from 'primevue/button'
// import Slider from 'primevue/slider';
// import Rating from 'primevue/rating';
// import {Form} from '@primevue/forms'
import QuestionBox from './QuestionBox.vue'

// import RadioButton from 'primevue/radiobutton';
import {inject, ref} from "vue";
const questions = inject('questions')

// Create a reactive array to keep track of answers (e.g., scores)
const answers = ref(Array(questions.length).fill(null));

// Handle response count updates
const handleResponse = (index, count) => {
  responses.value[index] = count;
};

// Form submit handler
const handleSubmit = () => {
  console.log('Aantal reacties per vraag:', responses.value);
  alert('Formulier is verzonden!');
};
</script>