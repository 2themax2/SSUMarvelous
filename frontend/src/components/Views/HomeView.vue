<script setup>
import Button from "primevue/button";
import Card from "primevue/card";
import Divider from "primevue/divider";
</script>

<template>
  <div class="home-view">
    <!-- Header Section -->
    <header class="header-section">
      <h1 class="text-center">Welkom bij ProjectHub</h1>
      <p class="text-center">
        Samenwerken aan een betere toekomst door interdisciplinaire projecten!
      </p>
    </header>

    <!-- Introduction Section -->
    <Card class="mt-3">
      <template #title>Over ProjectHub</template>
      <template #content>
        <p>
          In de 21ste eeuw komen we als samenleving in aanraking met complexere
          problemen door onder andere globalisering. Dit vraagt om
          professionals die interdisciplinair kunnen samenwerken om zo tot
          innovatieve oplossingen te komen.
        </p>
        <p>
          Dit platform biedt een omgeving waarin studenten van verschillende
          opleidingen samen kunnen werken aan projecten, begeleid door
          docenten. Met ProjectHub leggen we de basis voor interdisciplinaire
          samenwerking en innovatie.
        </p>
      </template>
    </Card>

    <Divider align="left">Doelstellingen</Divider>
    <!-- Objectives Section -->
    <Card class="objectives-list">
      <template #content>
        <ul>
          <li>Studenten interdisciplinair laten samenwerken.</li>
          <li>
            Diverse studentengroepen aan interdisciplinaire complexe vraagstukken
            laten werken.
          </li>
        </ul>
      </template>
    </Card>

    <Divider align="left">Impact van de oplossing</Divider>
    <!-- Impact Section -->
    <Card>
      <template #title>Impact</template>
      <template #content>
        <p>
          Studenten verbreden hun samenwerking skills, netwerk en denkniveau
          door met andere disciplines samen te werken en tot ideeën te komen.
        </p>
        <p>
          Door tijdens een opleiding interdisciplinair gewerkt te hebben ligt de
          lat lager om dit later, tijdens onderzoek of werk, weer te doen.
        </p>
      </template>
    </Card>

    <!-- Footer Section -->
    <footer class="footer-section mt-3 text-center">
      <p>
        Klaar om mee te doen? <strong>ProjectHub</strong> is hier om jouw
        projectervaring naar een hoger niveau te tillen.
      </p>
      <Button label="Ontdek meer" class="p-button-success" />
    </footer>
  </div>
</template>
