<script setup>
import Button from "primevue/button";
import Card from "primevue/card";
import Divider from "primevue/divider";
</script>

<template>
  <div class="home-view">
    <!-- Header Section -->
    <header class="header-section text-center">
      <img src="/src/assets/favicon.ico" alt="ProjectHub Logo" class="logo" />
      <h1>Welcome to ProjectHub</h1>
      <p>
        Collaborating for a better future through interdisciplinary projects!
      </p>
    </header>

    <!-- Introduction Section -->
    <Card class="mt-3">
      <template #title>About ProjectHub</template>
      <template #content>
        <p>
          In the 21st century, society faces increasingly complex problems due to globalization, among other factors. This requires professionals 
          who can collaborate across disciplines to develop innovative solutions. However, in current education systems, students often work 
          primarily with peers from their own study programs. As a result, they rarely learn how to collaborate interdisciplinarily during 
          their studies. Once these students enter the workforce, they are required to work and communicate with people from various backgrounds. 
          They then face the challenge of learning how to understand and empathize with those who have different perspectives. This is where 
          ProjectHub offers a solution. The idea is that each faculty designates a specific period during which students from various programs 
          collaborate on a project, learning to work interdisciplinarily. Through ProjectHub, teachers can create projects, and students from 
          different programs can sign up to participate.
        </p>
      </template>
    </Card>

    <Card>
      <template #title>Impact</template>
      <template #content>
        <p>
          Students broaden their collaboration skills, network, and way of thinking by working with other disciplines to develop ideas. 
          Experiencing interdisciplinary collaboration during their studies lowers the barrier for applying these skills later in research or work.
        </p>
      </template>
    </Card>

  </div>
</template>

<style>
.logo {
  max-width: 150px;
  margin-bottom: 1rem;
}
</style>
