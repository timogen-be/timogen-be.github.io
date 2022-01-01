<template>
  <div id="app">
    <h1 class="container">Timogen</h1>
    <div class="container p-5 my-5 border bg-white text-dark">
      <h2>Thérapeute</h2>
      <Therapist></Therapist>
      <hr />
      <h2>Patient</h2>
      <Patient></Patient>
      <hr />
      <h2>Mutuelle</h2>
      <Mutuality></Mutuality>
      <hr>
      <h2>Patho</h2>
      <Patho></Patho>
    </div>
  </div>
</template>

<script>
import Therapist from "./components/Therapist.vue";
import Patient from "./components/Patient.vue";
import Mutuality from "./components/Mutuality.vue";
import Patho from "./components/Patho.vue";


export default {
  name: "App",
  components: {
    Therapist,
    Patient,
    Mutuality,
    Patho
},
  // parent component
  computed: {
    // authHeaders() {
    //   return {
    //     Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1Ni....",
    //   };
    // },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
}
h1 {
  text-align: center;
  color: #cecece;
}

h2 {
  padding: 20px 0px 30px 0px;
}
</style>
