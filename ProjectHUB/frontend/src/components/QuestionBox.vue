<template>
  <div>
    <p>
      {{question.question}}
    </p>
    <div>
      <label v-for="score in 5" :key="score">
        <input
          type="radio"
          :value="score"
          name="response"
          @change="updateAnswer(score)"
        />
        {{ score }}
      </label>
    </div>
    <p>Jouw antwoord: {{ currentAnswer || 'Nog geen antwoord' }}</p>
  </div>


</template>

<script setup>
import { ref, defineProps } from 'vue';
defineProps(['question']);
const emit = defineEmits(['answered']);

// Houd het huidige antwoord bij
const currentAnswer = ref(null);

// Update het antwoord en stuur het door naar de ouder
const updateAnswer = (score) => {
  currentAnswer.value = score;
  emit('answered', score);
};
</script>

<style scoped>

</style>