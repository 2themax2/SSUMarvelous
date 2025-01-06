<template>
  <div>
    <p>
<!--      {{question.question}}-->
      {{question}}
    </p>
    <div class="flex flex-wrap gap-4">
<!--      <RadioButtonGroup>-->
        <div v-for="score in 5" :key="score" class="flex flex-wrap gap-4">
          <div class="flex align-items-center gap-2">
            <RadioButton size="small" v-model="selectedScore" :inputId="score.toString()" :value="score" name="response" @change="updateAnswer()"/>
            <label :for="score">{{score}}</label>
          </div>
        </div>
<!--      </RadioButtonGroup>-->
    </div>
  </div>


</template>

<script setup>
import RadioButton from 'primevue/radiobutton';
import {RadioButtonGroup} from "primevue";
import { ref, defineProps } from 'vue';

defineProps(['question']);
const emit = defineEmits(['answered']);
const selectedScore = ref(null)
const updateAnswer = () => {
  emit('answered', selectedScore);
};

</script>