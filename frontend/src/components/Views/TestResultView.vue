<script setup>

import {inject, onMounted, ref} from "vue";
import axios from "axios";
import { useRoute, useRouter } from 'vue-router'

const router = useRouter()
const route = useRoute()

const questions = ref([])
const result = "You are a Plant!"
const explanation = `In Belbin's team roles theory, a "Plant" is a creative and innovative thinker who brings fresh ideas and problem-solving strategies to a team. Plants are known for their originality but may sometimes struggle to turn their concepts into reality or communicate effectively without support from others.`;

</script>

<template>
  <header class="header-section">
    <h1 class="text-center">Test Result</h1>
  </header>
  <div class="result-card">
    <p class="result-text">{{ result }}</p>
    <p class="result-explanation">{{ explanation }}</p>
  </div>
</template>

<style scoped>
.header-section {
  margin-bottom: 20px;
}

.text-center {
  text-align: center;
}

.result-card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center; /* Centers text inside the card */
  margin: 20px auto; /* Centers the card horizontally */
  padding: 20px;
  max-width: 400px; /* Sets a max width for the card */
  background-color: white; /* Card background */
  border: 1px solid #ddd; /* Border for the card */
  border-radius: 8px; /* Rounded corners */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow effect */
}

.result-text {
  font-size: 20px;
  font-weight: bold;
  color: #2c3e50; /* Darker color for visibility */
  margin-bottom: 10px;
}

.result-explanation {
  font-size: 16px;
  color: #555; /* Softer text color */
  line-height: 1.5;
}
</style>