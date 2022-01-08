<template>
  <div id="app">
    <!-- <p>mutuality.name = {{mutuality.name}} </p> -->

    <h1>Timogen</h1>
    <div class="container p-5 my-5 border bg-white text-dark">
      <h2>Thérapeute</h2>
      <Therapist @receive="receiveTherapist" :therapist="therapist"></Therapist>
      <hr />

      <h2>Patient</h2>
      <Patient
        @receive="receivePatient"
        :patient="patient"
        :mutuality="mutuality"
      ></Patient>
      <br />
      <hr />
      <br />

      <Patho @receive="receivePatho"></Patho>
      <hr />

      <h2>Séances</h2>
      <Seances @receive="receiveSeances"></Seances>
      <br />

      <button
        type="button"
        class="container-fluid btn btn-secondary"
        @click="retrievePDF"
      >
        Générer mon justificatif
      </button>
    </div>
  </div>
</template>

<script>
import Therapist from "./components/Therapist.vue";
import Patient from "./components/Patient.vue";
import Patho from "./components/Patho.vue";
import Seances from "./components/Seances.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    Therapist,
    Patient,
    Patho,
    Seances,
  },
  data() {
    return {
      therapist: {
        address: "",
        bank_account: "",
        bce: "",
        contracted: false,
        id: 0,
        inami_nb: "",
        name: "",
      },
      patient: {
        name: "",
        niss: "",
        address: "",
      },
      mutuality: {
        name: "",
        address: "",
      },
      location: String,
      patho: String,
      dates: [],
      first_seance: 1,
    };
  },
  // parent component
  methods: {
    receiveTherapist(therapist) {
      this.therapist = therapist;
    },
    receivePatient(patient, mutuality) {
      this.patient = patient;
      this.mutuality = mutuality;
    },
    receivePatho(location, patho) {
      this.location = location;
      this.patho = patho;
    },
    receiveSeances(first_seance, dates) {
      this.first_seance = first_seance;
      this.dates = [];
      this.dates = dates;
    },
    retrievePDF() {
      var csrftoken = this.$cookies.get("csrftoken");
      let my_value = new TextEncoder("utf-8").encode(
        JSON.stringify({
          therapist: this.therapist,
          patient: this.patient,
          location: this.location,
          patho: this.patho,
          first_seance: this.first_seance,
          dates: this.dates,
        })
      );
      let url_with_params = "http://127.0.0.1:8000/api/timogen/pdf";

      const requestOptions = {
        method: "POST",
        headers: {
          "Content-type": "application/json",
          Cookies: "csrfmiddlewaretoken=" + csrftoken + ";",
        },
        body: my_value,
        responseType: "blob",
      };

      fetch(url_with_params, requestOptions)
        .then(function (response) {
          var file = new Blob([response.data]);
          //var file = data['response'];
          var fileURL = URL.createObjectURL(file);
          console.log(fileURL);
          window.open(fileURL, '_blank');
        })
        .catch(function (error) {});

      // console.log(my_value);

      // var datauri = "data:application/pdf;base64," + Base64.encode(data);
      // var win = window.open(
      //   "",
      //   "Your PDF",
      //   "width=1024,height=768,resizable=yes,scrollbars=yes,toolbar=no,location=no,directories=no,status=no,menubar=no,copyhistory=no"
      // );
      // win.document.location.href = datauri;
    },
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
  color: #3f7a82;
}

h2 {
  padding: 20px 0px 30px 0px;
}

h2,
h3,
h4,
h5 {
  color: darkgrey;
}

.bg-cyan {
  background-image: url("assets/60-lines.png");
  background-color: #beedf7;
}
</style>
